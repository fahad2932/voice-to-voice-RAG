# config.py

# LM Studio OpenAI-compat endpoint (running on localhost:1234)
API_BASE_URL = "http://localhost:1234/v1"        # :contentReference[oaicite:3]{index=3}
API_KEY      = "lm-studio"

# Vault & RAG settings
VAULT_PATH = "vault.txt"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K      = 3

# Audio settings
SAMPLE_RATE   = 16000  # Hz (compatible with webrtcvad) :contentReference[oaicite:4]{index=4}
FRAME_DURATION_MS = 30  # Must be 10, 20, or 30 ms :contentReference[oaicite:5]{index=5}
VAD_MODE      = 1       # 0–3 aggressiveness :contentReference[oaicite:6]{index=6}

# OpenVoice TTS endpoint
TTS_URL = "http://localhost:50021/tts"
