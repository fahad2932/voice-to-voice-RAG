# audio.py

import queue
import threading
import numpy as np
import sounddevice as sd                    # for audio I/O :contentReference[oaicite:3]{index=3}
import torch
from silero_vad import (load_silero_vad, read_audio,
                        get_speech_timestamps, VADIterator,
                        collect_chunks)
from config import SAMPLE_RATE, FRAME_DURATION_MS

# 
# This loads a JIT-quantized model (~2 MB) optimized for CPU inference.
# It returns the model and a tuple of helper functions.
# - get_speech_timestamps: returns speech segments
# - read_audio: reads .wav into float32 tensor
# - collect_chunks/VADIterator: streaming helpers
model, utils = torch.hub.load(
    repo_or_dir='snakers4/silero-vad',
    model='silero_vad',
    trust_repo=True
)                                          # :contentReference[oaicite:4]{index=4}
(get_speech_timestamps, _, read_audio,
 VADIterator, collect_chunks) = utils

_audio_queue = queue.Queue()

# -----------------------------------------------------------------------------
# Audio callback to feed raw PCM into queue
# -----------------------------------------------------------------------------
def _audio_callback(indata, frames, time, status):
    """Push raw 16-bit PCM frames into a queue for VAD processing."""
    if status:
        print(f"Audio status: {status}")
    # indata is float32 by default; convert to int16 PCM
    pcm = (indata * 32767).astype(np.int16)
    _audio_queue.put(pcm.tobytes())

def start_stream():
    """Begin non-blocking microphone capture at SAMPLE_RATE Hz."""
    stream = sd.InputStream(
        samplerate=SAMPLE_RATE,
        blocksize=int(SAMPLE_RATE * FRAME_DURATION_MS / 1000),
        dtype='float32',
        channels=1,
        callback=_audio_callback
    )                                        # :contentReference[oaicite:5]{index=5}
    stream.start()
    return stream

# -----------------------------------------------------------------------------
# Voice activity detection generator using Silero VAD
# -----------------------------------------------------------------------------
def voice_activity_generator():
    """
    Yields raw audio bytes for each detected speech segment.
    Internally accumulates 30 ms chunks until silence is detected.
    """
    buffer = bytearray()
    iterator = VADIterator(
        get_speech_timestamps=get_speech_timestamps,
        read_audio=lambda x: x,  # we supply raw PCM directly
        sampling_rate=SAMPLE_RATE,
        speech_pad_ms=200
    )                                        # :contentReference[oaicite:6]{index=6}

    while True:
        frame = _audio_queue.get()
        # iterator accepts raw PCM bytes; returns list of speech timestamps (samples)
        speech_windows = iterator([frame])
        if speech_windows:
            buffer.extend(frame)
        elif buffer:
            yield bytes(buffer)
            buffer.clear()

# -----------------------------------------------------------------------------
# noise reduction placeholder
# -----------------------------------------------------------------------------
def reduce_noise(audio_bytes):
    """
    Basic DC offset removal: subtract median to center waveform.
    For production, swap in a spectral denoiser.
    """
    arr = np.frombuffer(audio_bytes, dtype=np.int16)
    arr = arr - np.median(arr)              # crude noise floor removal
    return arr.tobytes()
