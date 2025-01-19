import os
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

def process_question(question: str) -> str:
    openai_api_key = os.getenv("OPENAI_API_KEY")
    qa_chain = load_qa_chain(OpenAI(model="text-davinci-003", api_key=openai_api_key))
    answer = qa_chain.run({"question": question})
    return answer