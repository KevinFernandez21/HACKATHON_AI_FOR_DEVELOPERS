import google.generativeai as genai 
from dotenv import load_dotenv
import os
load_dotenv()  # Load the .env file

genai.configure(api_key = os.getenv('API_KEY'))

model = genai.GenerativeModel('gemini-1.5-pro')
print(model)

