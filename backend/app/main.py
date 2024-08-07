from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import time
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware

# Load the .env file
load_dotenv()

# Configure the API key for genai
api_key = os.getenv('API_KEY_GEMINI')
if not api_key:
    raise ValueError("API_KEY not found in environment variables")
genai.configure(api_key=api_key)

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestBody(BaseModel):
    prompt: str

@app.post("/generate")
def generate_content(request: RequestBody):
    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction="Solo puedes decir dos palabras cuando yo te hable de comida me diras (comida) cuando yo te hable de computadoras tu me dices tecnologia cuando no hable de ninguna de la dos dime puedes repetir lo mencionado ")
        start_time = time.time()
        response = model.generate_content(request.prompt)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return {"response": response.text, "elapsed_time": elapsed_time}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
