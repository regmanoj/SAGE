# rag.py
from typing import Dict, List
from .llm import LLMWrapper
from .retriever import Retriever
import logging

logger = logging.getLogger(__name__)

class RAGPipeline:
    def __init__(self):
        self.llm = LLMWrapper()
        self.retriever = Retriever()
    
    def answer_query(self, query: str) -> Dict:
        try:
            # Get relevant passages
            contexts = self.retriever.get_relevant_context(query)
            
            if not contexts:
                return {
                    "answer": "No relevant information found.",
                    "sources": [],
                    "confidence": 0.0
                }
            
            # Combine contexts based on relevance scores
            combined_context = "\n".join([ctx[0] for ctx in contexts])
            confidence = sum([ctx[1] for ctx in contexts]) / len(contexts)
            
            # Generate response using LLM
            answer = self.llm.generate_response(query, combined_context)
            
            return {
                "answer": answer,
                "sources": [ctx[0] for ctx in contexts],
                "confidence": confidence
            }
            
        except Exception as e:
            logger.error(f"Error in RAG pipeline: {str(e)}")
            return {
                "answer": "Error processing query",
                "sources": [],
                "confidence": 0.0
            }