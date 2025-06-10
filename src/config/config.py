import os

class Config:
    OUTPUT_DIR = "output"
    THEOREMS_PATH = os.path.join("data", "easy_20.json")
    CONTEXT_LEARNING_PATH = "data/context_learning"
    CHROMA_DB_PATH = "data/rag/chroma_db"
    MANIM_DOCS_PATH = "data/rag/manim_docs"
    EMBEDDING_MODEL = "azure/text-embedding-3-large"
    
    # Kokoro TTS configurations
    KOKORO_MODEL_PATH="models/kokoro-v0_19.onnx"
    KOKORO_VOICES_PATH="models/voices.bin"
    KOKORO_DEFAULT_VOICE="af"
    KOKORO_DEFAULT_SPEED="1.0"
    KOKORO_DEFAULT_LANG="en-us"