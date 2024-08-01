import google.generativeai as genai 
from dotenv import load_dotenv
import os
import time

load_dotenv()  # Load the .env file

genai.configure(api_key=os.getenv('API_KEY'))

model = genai.GenerativeModel('gemini-1.5-flash')# 'gemini-1.5-pro' 

# Start the timer
start_time = time.time()

response = model.generate_content("Podrias darme recomendaciones para poder realizar un proyecto de inteligencia artificial?")

# End the timer
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print(response.text)
print(f"Tiempo de respuesta: {elapsed_time} segundos")