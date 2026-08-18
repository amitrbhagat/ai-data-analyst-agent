from app.llm.provider import provide_response


prompt = """
    Say Hello and tell me something aboot Large Language models and 
    give the classic examples of LLM's.
    """


response = provide_response(prompt, temperature=0.3)

print(response)
