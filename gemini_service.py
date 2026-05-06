from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_questions(topic, num=5):
    prompt = f"""
    Generate {num} multiple-choice questions about {topic}.
    Each question must have 4 choices (A-D) and correct answer.

    Format:
    Q:
    A.
    B.
    C.
    D.
    Answer:
    """

    response = client.models.generate_content(
        model="Gemini 2.5 Flash",
        contents=prompt
    )

    return response.text