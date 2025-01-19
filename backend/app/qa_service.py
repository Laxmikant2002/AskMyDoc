import os
import logging
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI
from openai import OpenAIError, RateLimitError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_question(question: str) -> str:
    openai_api_key = os.getenv("OPENAI_API_KEY")
    qa_chain = load_qa_chain(OpenAI(model="gpt-3.5-turbo", api_key=openai_api_key), chain_type="stuff")
    try:
        answer = qa_chain.invoke({"input_documents": [], "question": question})
    except RateLimitError:
        logger.error("Rate limit exceeded")
        return "You have exceeded your current quota. Please check your plan and billing details."
    except OpenAIError as e:
        logger.error(f"OpenAI error: {str(e)}")
        return f"An error occurred: {str(e)}"
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return f"An unexpected error occurred: {str(e)}"
    return answer