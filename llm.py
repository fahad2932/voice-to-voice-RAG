# llm.py

import os, openai
from config import API_BASE_URL, API_KEY

openai.api_base = API_BASE_URL
openai.api_key  = API_KEY

def ask(prompt: str) -> str:
    resp = openai.ChatCompletion.create(
        model="mistral-7b-instruct",
        messages=[{"role":"system","content":"You are a helpful assistant."},
                  {"role":"user",  "content":prompt}],
        temperature=0.7,
        max_tokens=512,
        stream=False
    )
    return resp.choices[0].message.content.strip()
