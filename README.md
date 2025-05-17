# Real-Time Voice Assistant (Emma)

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

## 🏗️ Architecture
```mermaid
flowchart TB
  %% Inputs
  A[🎤 Microphone Input]
  
  %% Preprocessing
  A --> B[🔴 Silero VAD<br/>(Voice Activity Detection)]
  B --> C[▶️ Audio Segment<br/>(start/end detected)]
  C --> D[🧹 Noise Reduction & Preprocessing]
  
  %% ASR + Command Parsing
  D --> E[🦊 Whisper Transcription<br/>(faster-whisper)]
  E --> F[🗣️ Command Parser]
  F --> |"insert info ..."| G[📁 Append into vault.txt]
  F --> |"print info"| H[📖 Read & return vault content]
  F --> |"delete info"| I[🗑️ Clear vault<br/>(with optional confirm)]
  F --> |(else query)| J[💡 Trigger RAG flow]
  
  %% RAG + Retrieval
  J --> K[🏛️ Vault Embedding Lookup<br/>(sentence-transformers)]
  K --> L[🔍 Top-K Semantic Retrieval<br/>(cosine sim)]
  
  %% LLM + TTS
  L --> M[✍️ Prompt Construction<br/>(context + user query)]
  M --> N[🤖 LLM Response<br/>(Mistral 7B via LM Studio API)]
  N --> O[🔊 Text-to-Speech<br/>(OpenVoice TTS)]
  O --> P[🔈 Speak Response Back to User]

    
                              ▼

                              ▼
🔊 Speak Response Back to User
</details>
