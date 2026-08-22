from app.utils.validation import validate_question


# Valid question
question = "What is the total revenue?"

try:
    result = validate_question(question)
    print("VALID:", result)
except ValueError as e:
    print("REJECTED:", e)


# Empty question
try:
    validate_question("")
except ValueError as e:
    print("EMPTY QUESTION:", e)


# Malicious input
try:
    validate_question("'; DROP TABLE customers; --")
except ValueError as e:
    print("MALICIOUS INPUT:", e)


# Too long question
try:
    validate_question("A" * 1001)
except ValueError as e:
    print("LONG QUESTION:", e)