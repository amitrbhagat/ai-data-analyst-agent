from dataclasses import dataclass
import re
import sqlparse
from sqlparse.sql import Identifier, IdentifierList
from sqlparse.tokens import Keyword, DML


@dataclass
class ValidationResult:
    is_valid: bool
    error_message: str | None = None
    sql: str | None = None


# Only these tables are allowed to be referenced.
ALLOWED_TABLES = {
    "regions",
    "customers",
    "products",
    "orders",
    "order_items",
}

MAX_ROWS = 1000


# Secondary defense-in-depth blocklist.
BLOCKED_KEYWORDS = {
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "GRANT",
    "REVOKE",
    "EXECUTE",
    "MERGE",
    "CALL",
    "COPY",
}


def _contains_blocked_keyword(sql: str) -> str | None:
    """
    Look for dangerous SQL keywords and comment injection patterns.
    """

    # SQL comments are not needed for our generated queries.
    if "--" in sql:
        return "--"

    if "/*" in sql or "*/" in sql:
        return "/* or */"

    for keyword in BLOCKED_KEYWORDS:
        pattern = rf"\b{re.escape(keyword)}\b"

        if re.search(pattern, sql, re.IGNORECASE):
            return keyword

    return None


def _extract_table_names(statement) -> set[str]:
    """
    Extract table names appearing after FROM or JOIN.

    This intentionally focuses on the tables our application expects
    instead of trying to interpret every possible SQL construct.
    """

    tables = set()
    tokens = list(statement.flatten())

    expect_table = False

    for token in tokens:

        value = token.value.strip()
        upper_value = value.upper()

        if not value:
            continue

        # FROM / JOIN means the next identifier represents a table.
        if upper_value in {"FROM", "JOIN"}:
            expect_table = True
            continue

        if expect_table:

            # Ignore whitespace.
            if token.is_whitespace:
                continue

            # Handle comma-separated tables.
            if upper_value == ",":
                expect_table = True
                continue

            # Ignore SQL keywords.
            if token.ttype in Keyword:
                expect_table = False
                continue

            # Extract the first identifier.
            table_name = value.split(".")[-1]

            # Remove quoting if present.
            table_name = table_name.strip('"').strip("'").lower()

            # Remove alias if accidentally included.
            table_name = table_name.split()[0]

            tables.add(table_name)

            expect_table = False

    return tables


def _has_limit(sql: str) -> bool:
    """
    Check whether the query already contains a LIMIT clause.
    """

    return bool(re.search(r"\bLIMIT\s+\d+\b", sql, re.IGNORECASE))


def validate_sql(sql: str) -> ValidationResult:
    """
    Validate LLM-generated SQL before execution.

    Rules:
    1. Only SELECT / WITH queries.
    2. No multiple statements.
    3. No dangerous keywords/comments.
    4. Only known application tables.
    5. Automatically enforce LIMIT 1000.
    """

    # ---------------------------------------------------------
    # 1. Basic input validation
    # ---------------------------------------------------------

    if not sql or not sql.strip():
        return ValidationResult(
            is_valid=False,
            error_message="SQL query is empty."
        )

    sql = sql.strip()

    # ---------------------------------------------------------
    # 2. Reject semicolons
    # ---------------------------------------------------------

    # Simplest and safest approach:
    # our generated SQL must not contain semicolons.
    if ";" in sql:
        return ValidationResult(
            is_valid=False,
            error_message="Semicolons are not allowed. Multiple SQL statements are rejected."
        )

    # ---------------------------------------------------------
    # 3. Parse SQL
    # ---------------------------------------------------------

    statements = sqlparse.parse(sql)

    if len(statements) != 1:
        return ValidationResult(
            is_valid=False,
            error_message="Multiple SQL statements are not allowed."
        )

    statement = statements[0]

    # ---------------------------------------------------------
    # 4. Statement type check
    # ---------------------------------------------------------

    first_keyword = None

    for token in statement.tokens:

        if token.is_whitespace:
            continue

        if token.ttype in Keyword or token.ttype in DML:
            first_keyword = token.value.upper()
            break

        # WITH is normally identified as a Keyword.
        if token.value.upper() == "WITH":
            first_keyword = "WITH"
            break

        break

    if first_keyword not in {"SELECT", "WITH"}:
        return ValidationResult(
            is_valid=False,
            error_message=(
                f"Only SELECT or WITH queries are allowed. "
                f"Detected: {first_keyword}"
            )
        )

    # ---------------------------------------------------------
    # 5. Block dangerous keywords / comments
    # ---------------------------------------------------------

    blocked = _contains_blocked_keyword(sql)

    if blocked:
        return ValidationResult(
            is_valid=False,
            error_message=f"Blocked SQL keyword or pattern detected: {blocked}"
        )

    # SELECT INTO can create a table.
    if re.search(r"\bSELECT\s+.*\bINTO\b", sql, re.IGNORECASE | re.DOTALL):
        return ValidationResult(
            is_valid=False,
            error_message="SELECT INTO is not allowed."
        )

    # ---------------------------------------------------------
    # 6. Table allowlist
    # ---------------------------------------------------------

    referenced_tables = _extract_table_names(statement)

    unknown_tables = referenced_tables - ALLOWED_TABLES

    if unknown_tables:
        return ValidationResult(
            is_valid=False,
            error_message=(
                "Query references unauthorized table(s): "
                + ", ".join(sorted(unknown_tables))
            )
        )

    # ---------------------------------------------------------
    # 7. LIMIT enforcement
    # ---------------------------------------------------------

    validated_sql = sql

    if not _has_limit(sql):
        validated_sql = f"{sql}\nLIMIT {MAX_ROWS}"

    # ---------------------------------------------------------
    # 8. Everything passed
    # ---------------------------------------------------------

    return ValidationResult(
        is_valid=True,
        error_message=None,
        sql=validated_sql
    )


    