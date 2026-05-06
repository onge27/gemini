 

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("Gemini 2.5 Flash")

response = model.generate_content("Explain Python in simple words")
print(response.text)