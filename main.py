# main.py

import asyncio
from audio import start_stream, voice_activity_generator, reduce_noise
from transcriber import transcribe
from commands import parse_and_execute
from vault import read_info
from retriever import get_top_k
from llm import ask
from tts import speak

async def process_segment(seg_bytes: bytes):
    clean = reduce_noise(seg_bytes)
    text  = transcribe(clean)
    print(f"> You: {text}")

    # command?
    resp = parse_and_execute(text)
    if resp is None:
        # RAG
        vault_txt = read_info().splitlines()
        context   = "\n".join(get_top_k(text, vault_txt))
        prompt    = f"{context}\nUser: {text}\nAssistant:"
        resp      = ask(prompt)
    print(f"< Emma: {resp}")
    speak(resp)

async def main():
    start_stream()
    loop = asyncio.get_event_loop()
    for seg in voice_activity_generator():
        # dispatch each segment without blocking audio capture
        asyncio.create_task(process_segment(seg))

if __name__ == "__main__":
    asyncio.run(main())
