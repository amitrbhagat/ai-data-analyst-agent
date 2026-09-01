from app.agents.prompts.intent_routing import build_routing_prompt
from app.llm.provider import provide_response


question = "How many customers do we have ?"

prompt = build_routing_prompt(question)

response = provide_response(
    prompt,
    temperature=0.0
)

print("LLM RESPONSE:")
print(response)
