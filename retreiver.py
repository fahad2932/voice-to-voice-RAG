# retriever.py

from sentence_transformers import SentenceTransformer
import numpy as np
from config import EMBED_MODEL, TOP_K

_embed_model = SentenceTransformer(EMBED_MODEL)

def get_top_k(query: str, corpus: list[str]) -> list[str]:
    if not corpus:
        return []
    corpus_emb = _embed_model.encode(corpus, convert_to_numpy=True)
    q_emb      = _embed_model.encode([query], convert_to_numpy=True)[0]
    scores = corpus_emb @ q_emb
    idx    = np.argsort(scores)[-TOP_K:][::-1]
    return [corpus[i] for i in idx]
