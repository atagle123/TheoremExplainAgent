import os
from dataclasses import dataclass, field
from typing import Optional
    
@dataclass
class ConfigDefaults:
    model: str = "anthropic/claude-3-5-sonnet-20240620"
    helper_model: Optional[str] = None
    only_gen_vid: bool = False
    only_combine: bool = False
    peek_existing_videos: bool = False
    output_dir: str = "output/my_exp_name"
    theorems_path: Optional[str] = None
    sample_size: Optional[int] = None
    verbose: bool = False
    max_retries: int = 5
    use_rag: bool = False
    use_visual_fix_code: bool = False
    chroma_db_path: str = "data/rag/chroma_db"
    manim_docs_path: str = "data/rag/manim_docs"
    embedding_model: str = "azure/text-embedding-3-large"
    use_context_learning: bool = False
    context_learning_path: str = "data/context_learning"
    use_langfuse: bool = False
    max_scene_concurrency: int = 1
    max_topic_concurrency: int = 1
    debug_combine_topic: Optional[str] = None
    only_plan: bool = False
    check_status: bool = False
    only_render: bool = False
    scenes: Optional[list[int]] = field(default_factory=list)
    topic: Optional[str] = None
    context: Optional[str] = None
    KOKORO_MODEL_PATH: str = "models/kokoro-v0_19.onnx"
    KOKORO_VOICES_PATH: str = "models/voices.bin"
    KOKORO_DEFAULT_VOICE: str = "af"
    KOKORO_DEFAULT_SPEED: str = "1.0"
    KOKORO_DEFAULT_LANG: str = "en-us"