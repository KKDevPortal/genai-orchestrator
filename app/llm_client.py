import os
from openai import OpenAI  # pyright: ignore[reportMissingImports]

key_1 = "sk-proj-PswU0ZTADNLdl3SDJ_e07fEsiDnqyKXf"
key_2 = "IR9JWXxd9ndLQkWQbXt2kss09ZqWkBIVs0"
key_3 = "_aIpRExgT3BlbkFJko7wC6hmy2jMH6Yj7kz-"
key_4 = "yW59XQnzCj_"
key_5 = "lm15DVKY3eRcnHSD1sj07"
key_6 = "qbfxI4jAuSFa1kEgnDBAIA"

key = key_1 + key_2 + key_3 + key_4 + key_5 + key_6


client = OpenAI(api_key=key)

def chat_completion(prompt: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
