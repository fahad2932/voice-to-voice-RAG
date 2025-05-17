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
flowchart TD
    A[Microphone Input] --> B[Silero VAD (Voice Detection)]
    B --> C[Audio Preprocessing (Denoise, Trim)]
    C --> D[Whisper Transcription]
    D --> E{Command Type?}

    E -->|Insert Info| F[Append to vault.txt]
    E -->|Print Info| G[Read and Speak vault.txt]
    E -->|Delete Info| H[Delete vault.txt (with confirm)]
    E -->|Other Query| I[Retrieve Context from Vault Embeddings]

    I --> J[Top-K Matching (Cosine Similarity)]
    J --> K[Construct Prompt (Context + Query)]
    K --> L[LLM Response (via LM Studio)]
    L --> M[Text-to-Speech (OpenVoice)]
    M --> N[Speak Response to User]
