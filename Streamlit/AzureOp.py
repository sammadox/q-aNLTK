import os
from openai import AzureOpenAI

# Load environment variables from a .env file
from dotenv import load_dotenv
load_dotenv('.env')  # Adjust the path if your .env file is located elsewhere



def send_chat_message(messages):
    # Initialize the client using environment variables
    client = AzureOpenAI(
        api_key=os.getenv("724a9bfec68944fca09eaeb995b7014e"),
        api_version=os.getenv("2024-02-01"),
        azure_endpoint=os.getenv("https://dgopenaidev.openai.azure.com/")
    )

    response = client.chat.completions.create(
        model="DgOpenApiChat1Dev",
        messages=messages
    )

    return response


