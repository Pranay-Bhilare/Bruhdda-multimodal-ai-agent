from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

def get_chat_model(temperature: float = 0.7):
    return ChatGroq(
        api_key= os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile",
        temperature=temperature,
    )
