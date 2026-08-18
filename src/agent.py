import json
import urllib.request
import urllib.error

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"


def ask_agent(question):
    try:
        data = {
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful academic project assistant."
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            "stream": False
        }

        request = urllib.request.Request(
            OLLAMA_URL,
            data=json.dumps(data).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode("utf-8"))

        return result["message"]["content"]

    except urllib.error.URLError as e:
        return f"Could not connect to Ollama: {e}"

    except Exception as e:
        return f"Error: {e}"


print("===============================")
print(" Local AI Agent Started")
print(" Using Ollama - No API Key")
print("===============================")

while True:
    user_input = input("You: ")

    if user_input.strip().lower() == "exit":
        print("Agent: Goodbye!")
        break

    if not user_input.strip():
        continue

    answer = ask_agent(user_input)

    print("Agent:", answer)
    print("-------------------------------")