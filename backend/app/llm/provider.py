## In provider.py we are going to buld a abstraction layer 
## where our rest of the application is going to connect with AI model (LLM) through this abstraction layer


from app.llm.ollama import generate_response


prompt = """
    Instruction: Answer should be accurate and long enough
    Question: Tell me something about old India ?
    """


def provide_response(prompt: str, temperature: float = 0.7) -> str:
    response = generate_response(prompt, temperature)
    return response


# if __name__ == "__main__":
#     res = provide_response(prompt, temperature=0.3)
#     print("-----------------------------------------")
#     print(res)
