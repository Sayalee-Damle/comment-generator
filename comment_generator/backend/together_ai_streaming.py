import json
import os

import requests
import sseclient

url = "https://api.together.xyz/inference"
model = "togethercomputer/RedPajama-INCITE-7B-Chat"
prompt = "Tell me a story\n\n"

print(f"Model: {model}")
print(f"Prompt: {repr(prompt)}")
print("Repsonse:")
print()

payload = {
    "model": model,
    "prompt": prompt,
    "max_tokens": 512,
    "temperature": 0.7,
    "top_p": 0.7,
    "top_k": 50,
    "repetition_penalty": 1,
    "stream_tokens": True,
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
}

response = requests.post(url, json=payload, headers=headers, stream=True)
response.raise_for_status()

client = sseclient.SSEClient(response)
for event in client.events():
    if event.data == "[DONE]":
        break

    partial_result = json.loads(event.data)
    token = partial_result["choices"][0]["text"]
    print(token, end="", flush=True)     