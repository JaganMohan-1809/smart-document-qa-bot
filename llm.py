import os
import google.generativeai as genai
from dotenv import load_dotenv
from logger import setup_logger

logger = setup_logger()

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_llm(context, question):

    logger.info("Sending prompt to Gemini model")

    prompt = f"""
You are a helpful AI assistant.

Answer the QUESTION using ONLY the provided DOCUMENT.

If the answer is not in the document say:
"I could not find the answer in the document."

DOCUMENT:
{context}

QUESTION:
{question}

ANSWER:
"""

    response = model.generate_content(prompt)

    logger.info("Received response from Gemini")

    return response.text