# config.py
import os
from pathlib import Path

class Config:
    # Project paths
    ROOT_DIR = Path(os.path.dirname(os.path.dirname(__file__)))
    DATA_DIR = ROOT_DIR / "data"
    MODELS_DIR = ROOT_DIR / "models"
    
    # Bhagavad Gita files
    GITA_VERSES = DATA_DIR / "Bhagwad_Gita_Verses_English.csv"
    GITA_MEANINGS = DATA_DIR / "Gita_Word_Meanings_English.csv"
    GITA_CONCEPTS = DATA_DIR / "Bhagwad_Gita_Verses_Concepts.csv"
    GITA_QUESTIONS = DATA_DIR / "Bhagwad_Gita_Verses_English_Questions.csv"
    
    # Patanjali Yoga Sutras files
    YOGA_VERSES = DATA_DIR / "Patanjali_Yoga_Sutras_Verses_English.csv"
    YOGA_QUESTIONS = DATA_DIR / "Patanjali_Yoga_Sutras_Verses_English_Questions.csv"
    
    # Model settings
    MODEL_PATH = MODELS_DIR / "Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf"
    CONTEXT_LENGTH = 4096
    MAX_TOKENS = 512
    TEMPERATURE = 0.7
    
    # Vector store settings
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    
    # RAG settings
    TOP_K = 3
    SIMILARITY_THRESHOLD = 0.7