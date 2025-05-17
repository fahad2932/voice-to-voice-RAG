# tts.py

import requests, tempfile, os
from config import TTS_URL

def speak(text: str):
    resp = requests.post(TTS_URL, json={"text": text})
    resp.raise_for_status()
    # write and play
    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    tmp.write(resp.content)
    tmp.close()
    os.system(f"ffplay -nodisp -autoexit {tmp.name} >/dev/null 2>&1")
    os.unlink(tmp.name)
