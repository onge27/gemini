from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def generate_questions(topic):
    prompt = f"""
    Generate 5 multiple choice questions about {topic}.

    Format:
    Q1:
    A.
    B.
    C.
    D.
    Answer:
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text

print(generate_questions("Python basics"))