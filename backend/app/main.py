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
api_key = os.getenv('API_KEY')
if not api_key:
    raise ValueError("API_KEY not found in environment variables")
genai.configure(api_key=api_key)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
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
            system_instruction="You can only say 3 words Simple Complex and nothing, under your criteria you can say simple when the user asks for a simple task that does not need planning, you can say Complex when the user needs a schedule or many tasks and finally if neither of the two or both are the case say nothing, you are an App against procrastination and improving time control you cannot talk about anything else.")  
        start_time = time.time()
        response = model.generate_content(request.prompt)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return {"response": response.text, "elapsed_time": elapsed_time}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)