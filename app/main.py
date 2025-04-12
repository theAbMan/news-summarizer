from fastapi import FastAPI,Request
from pydantic import BaseModel
from app.summarizer import summarize_text

app = FastAPI()

class TextInput(BaseModel):
    text : str

@app.post("/summarize")
def summarize(input:TextInput):
    summary = summarize_text(input.text)
    return {"summary":summary}
