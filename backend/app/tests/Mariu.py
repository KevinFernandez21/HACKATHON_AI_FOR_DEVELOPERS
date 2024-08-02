## implementar fast API para crear un chat simple

import google.generativeai as genai 
from dotenv import load_dotenv
import os
import time

load_dotenv()  # Load the .env file

genai.configure(api_key=os.getenv('API_KEY'))

model = genai.GenerativeModel('gemini-1.5-flash')

# Start the timer
start_time = time.time()

response = model.generate_content("hola")

# End the timer
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print(response)
print(f"Tiempo de respuesta: {elapsed_time} segundos")