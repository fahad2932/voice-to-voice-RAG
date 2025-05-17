# transcriber.py

from faster_whisper import WhisperModel
import torch

# Load Whisper-base quantized for speed
_device = "cuda" if torch.cuda.is_available() else "cpu"
_model = WhisperModel("base", device=_device)

def transcribe(raw_audio_bytes):
    """
    raw_audio_bytes: 16-bit PCM @ 16 kHz.
    Returns joined transcript.
    """
    segments, _ = _model.transcribe(
        np.frombuffer(raw_audio_bytes, dtype=np.int16),
        beam_size=5,
        word_timestamps=False
    )
    return " ".join(segment.text for segment in segments)
