# genai-orchestrator

## Install
pip install fastapi uvicorn openai python-dotenv

## Run
uvicorn app.main:app --reload

## Where to get the OpenAI (ChatGPT) API Key
1️⃣ Go to OpenAI dashboard

👉 https://platform.openai.com/

(Login with the same account you use for ChatGPT)

2️⃣ Open API Keys page

Direct link:
👉 https://platform.openai.com/api-keys

3️⃣ Create a new API key

Click “Create new secret key”

Give it a name (e.g. genai-orchestrator)

Copy the key immediately



## Curl 
```
curl --location 'http://localhost:8000/ask' \
--header 'Content-Type: application/json' \
--data '{
    "question": "What is GenAI orchestration?"
  }'
```