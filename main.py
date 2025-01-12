# main.py
from src.rag import RAGPipeline
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    rag = RAGPipeline()
    print("Gita & Yoga Sutras RAG Chatbot")
    print("Type 'quit' to exit\n")
    
    while True:
        query = input("\nQuestion: ").strip()
        if query.lower() == 'quit':
            break
            
        result = rag.answer_query(query)
        print("\nAnswer:", result["answer"])
        print("\nSources:")
        for source in result["sources"]:
            print(f"- {source}")
        print(f"\nConfidence: {result['confidence']:.2f}")

if __name__ == "__main__":
    main()