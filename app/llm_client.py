import os
from openai import OpenAI  # pyright: ignore[reportMissingImports]

client = OpenAI(api_key="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")

def chat_completion(prompt: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
