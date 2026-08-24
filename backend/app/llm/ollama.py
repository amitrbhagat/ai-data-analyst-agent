import requests


def generate_response(prompt:str, temperature: float = 0.7) -> str:

    url = "http://localhost:11434/api/chat"

    payload = {
        "model" : "tinyllama:latest",

        "messages": [
            {"role":"user", "content":prompt}
        ],

        "options": {
            "temperature": temperature
        },

        "stream":False,

        "format":"json"
    }


    try :
        response = requests.post(url, json=payload)
        response.raise_for_status()

        data = response.json()
        # print(f"data is : {data}")
        # print(data["created_at"])

        generated_text = data["message"]["content"]
        return generated_text

    except requests.exceptions.RequestException as e:

        print(f"Error occured {e}")   
        return ""




OLLAMA_BASE_URL = "http://localhost:11434"

def generate_embedding(text: str) -> list[float]:
    """
    Generate an embedding vector using Ollama.
    """

    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/embed",
        json={
            "model": "nomic-embed-text",
            "input": text,
        },
        timeout=60,
    )

    response.raise_for_status()

    data = response.json()
    
    return data["embeddings"][0]




# if __name__ == "__main__":

#     my_prompt = """
#     Instruction: Give the accurate answer
#     Question: Tell me something about India
#     """

#     res = generate_response(my_prompt, temperature=0.3)
#     print("-----------------")
#     print(res)
            