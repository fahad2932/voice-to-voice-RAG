# Real-Time Voice Assistant 

A fully local, modular voice-driven assistant that captures your microphone in real time, transcribes speech with Whisper (via faster-whisper/CTranslate2), manages contextual “vault” notes, retrieves relevant context via embeddings, queries a local LLM (Mistral 7B in LM Studio), and speaks responses using OpenVoice TTS—all orchestrated by simple voice commands.

---

## 🔍 Features

- **Voice Activity Detection**  
  Silero VAD + `sounddevice` for accurate, low-latency speech segmentation.

- **Automatic Transcription**  
  Faster-Whisper (CTranslate2) for near real-time ASR.

- **Voice Commands & Vault**  
  `insert info`, `print info`, `delete info` to manage a local text vault.

- **Retrieval-Augmented Generation**  
  Sentence-Transformer embeddings + top-K cosine retrieval (K=3) for contextual prompts.

- **Local LLM Inference**  
  Mistral 7B via LM Studio’s OpenAI-compatible API for fast, private generation.

- **Text-to-Speech**  
  OpenVoice TTS for ultra-low latency spoken responses.
