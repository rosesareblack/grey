from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llama_cpp import Llama
import os
MODEL_PATH = "/models/mistral-7b-instruct-v0.3.Q4_K_M.gguf"
llm = Llama(
model_path=MODEL_PATH,
n_gpu_layers=35,          # adjust to your VRAM
n_ctx=32768,              # max context
verbose=False
)
app = FastAPI(title="Mistral-Uncensored")
class Message(BaseModel):
role: str
content: str
class ChatRequest(BaseModel):
messages: list[Message]
temperature: float = 0.7
max_tokens: int = 1024
stream: bool = False
@app.post("/v1/chat/completions")
def chat(req: ChatRequest):
try:
msgs = [{"role": m.role, "content": m.content} for m in req.messages]
output = llm.create_chat_completion(
messages=msgs,
temperature=req.temperature,
max_tokens=req.max_tokens,
stream=req.stream
)
return output
except Exception as e:
raise HTTPException(status_code=500, detail=str(e))
healthcheck

@app.get("/")
def root():
return {"status": "ok", "model": MODEL_PATH.split("/")[-1]}
