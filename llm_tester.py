from src.llm import LLMWrapper
import logging

logging.basicConfig(level=logging.INFO)

def test_llm():
    llm = LLMWrapper()
    test_prompt = "What is the meaning of life?"
    
    try:
        response = llm.generate_response(
            prompt=test_prompt,
            context="Life's meaning is deeply personal and philosophical."
        )
        print(f"Test Prompt: {test_prompt}")
        print(f"Response: {response}")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    test_llm()