#llm.py
from llama_cpp import Llama
from typing import Dict, List
import logging
from .config import Config

logger = logging.getLogger(__name__)

class LLMWrapper:
    def __init__(self):
        self.model = Llama(
            model_path=str(Config.MODEL_PATH),
            n_ctx=Config.CONTEXT_LENGTH,
            n_threads=4
        )
        
    def generate_response(self, prompt: str, context: str) -> str:
        try:
            full_prompt = f"""Context: {context}

Question: {prompt}

Answer based on the context provided. If the context doesn't contain relevant information, say so.

Answer:"""
            
            response = self.model(
                full_prompt,
                max_tokens=Config.MAX_TOKENS,
                temperature=Config.TEMPERATURE,
                stop=["Question:", "\n\n"]
            )
            return response['choices'][0]['text'].strip()
            
        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return "Error generating response. Please try again."
            
    def get_system_info(self) -> Dict:
        return {
            "model_path": str(Config.MODEL_PATH),
            "context_length": Config.CONTEXT_LENGTH,
            "max_tokens": Config.MAX_TOKENS
        }