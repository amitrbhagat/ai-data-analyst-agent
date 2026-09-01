import json

from pydantic import ValidationError

from app.agents.prompts.intent_routing import build_routing_prompt
from app.llm.provider import provide_response
from app.schemas.routing import RoutingResult


def classify_intent(question: str) -> RoutingResult:
    """
    Classify the user's question into:
    SQL, RAG, or HYBRID.
    """

    # 1. Build routing prompt
    prompt = build_routing_prompt(question)

    # 2. Send prompt to LLM
    response = provide_response(
        prompt,
        temperature=0.0
    )

    # 3. Remove markdown fences if the model adds them
    response = response.strip()

    if response.startswith("```"):
        lines = response.splitlines()

        # Remove first line: ```json
        if lines:
            lines = lines[1:]

        # Remove last line: ```
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        response = "\n".join(lines).strip()

    # 4. Parse JSON
    try:
        parsed_response = json.loads(response)

    except json.JSONDecodeError as e:
        raise ValueError(
            "LLM returned invalid routing JSON."
        ) from e

    # 5. Normalize route capitalization
    if "route" in parsed_response:
        parsed_response["route"] = (
            str(parsed_response["route"]).upper()
        )

    # 6. Validate with Pydantic
    try:
        result = RoutingResult(**parsed_response)

    except ValidationError as e:
        raise ValueError(
            "Invalid routing response from LLM."
        ) from e

    return result
