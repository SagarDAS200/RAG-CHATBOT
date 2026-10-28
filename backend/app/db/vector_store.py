import os
from pathlib import Path

from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from app.core.config import settings

# Process-local cache so upload + chat share the same store in one server process.
_store: InMemoryVectorStore | None = None


def _build_embeddings() -> OpenAIEmbeddings:
    """OpenRouter embeddings (same design as before)."""
    return OpenAIEmbeddings(
        model="nvidia/nemotron-3-embed-1b:free",
        openai_api_key=settings.OPENAI_API_KEY,
        base_url="https://openrouter.ai/api/v1",
        check_embedding_ctx_length=False,
    )


def get_vector_store() -> InMemoryVectorStore:
    """
    Returns a shared InMemoryVectorStore, loading from JSON if present.
    Missing or unreadable files yield an empty store (safe for first run).
    Does not use ChromaDB / gRPC.
    """
    global _store
    if _store is not None:
        return _store

    embeddings = _build_embeddings()
    path = settings.VECTOR_STORE_PATH

    if os.path.isfile(path) and os.path.getsize(path) > 0:
        try:
            _store = InMemoryVectorStore.load(path, embeddings)
        except Exception:
            # Corrupt/empty/unreadable JSON: start fresh rather than crash startup.
            _store = InMemoryVectorStore(embeddings)
    else:
        _store = InMemoryVectorStore(embeddings)

    return _store


def persist_vector_store(vector_store: InMemoryVectorStore | None = None) -> None:
    """Write the in-memory store to JSON (creates parent dirs as needed)."""
    store = vector_store or get_vector_store()
    path = settings.VECTOR_STORE_PATH
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    store.dump(path)


def get_store_size(vector_store: InMemoryVectorStore | None = None) -> int:
    """Number of stored chunks (portable replacement for Chroma _collection.count())."""
    store = vector_store or get_vector_store()
    return len(store.store)
