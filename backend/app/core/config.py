import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Production RAG API"
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    CHROMA_PERSIST_DIR: str = "./chroma_data"
    # JSON-backed InMemoryVectorStore path (separate from chroma_data)
    VECTOR_STORE_PATH: str = "./data/vector_store.json"
    CHUNK_SIZE: int = 512
    CHUNK_OVERLAP: int = 64

    class Config:
        env_file = ".env"

settings = Settings()
