from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Connect to OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def ask_agent(question):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=question
    )

    return response.output_text


# Main program
print("AI Agent Started!")
print("----------------")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
        break

    answer = ask_agent(user_input)

    print("Agent:", answer)
