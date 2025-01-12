# utils.py
import pandas as pd
from typing import List, Dict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_data(file_path: str) -> pd.DataFrame:
    """Load and preprocess CSV data"""
    try:
        df = pd.read_csv(file_path)
        logger.info(f"Successfully loaded {file_path}")
        return df
    except Exception as e:
        logger.error(f"Error loading {file_path}: {str(e)}")
        raise

def preprocess_text(text: str) -> str:
    """Clean and preprocess text"""
    return text.strip().lower()

def combine_verse_data(verses_df: pd.DataFrame, 
                      meanings_df: pd.DataFrame, 
                      concepts_df: pd.DataFrame) -> pd.DataFrame:
    """Combine verse data with meanings and concepts"""
    # Merge dataframes based on verse ID/chapter
    combined_df = verses_df.merge(meanings_df, on=['chapter', 'verse'], how='left')
    combined_df = combined_df.merge(concepts_df, on=['chapter', 'verse'], how='left')
    return combined_df