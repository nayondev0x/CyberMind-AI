import os
import subprocess
import requests
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# CyberMind AI - Path Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECTS_ROOT = os.path.join(BASE_DIR, "..", "projects")
BRAIN_STORAGE = os.path.join(BASE_DIR, "..", "neural_brain")

for path in [PROJECTS_ROOT, BRAIN_STORAGE]:
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

class ChatRequest(BaseModel):
    prompt: str
    project: str = "main_vault"

USAGE = {"tokens": 1240, "requests": 42, "limit": 1000000}

@app.get("/api/usage")
def get_usage():
    return USAGE

@app.post("/api/chat")
def chat(req: ChatRequest):
    USAGE["requests"] += 1
    USAGE["tokens"] += len(req.prompt) * 4
    prompt = req.prompt.lower()
    
    # Ultra-Pro Response Logic
    if "website" in prompt:
        code = "<html><body style='background:#050505; color:#3b82f7; font-family:sans-serif; display:flex; justify-content:center; align-items:center; height:100vh;'><h1>CyberMind AI Elite Build</h1><p>Created by NayonDev</p></body></html>"
        return {"response": "CyberMind AI has architected your build. Preview is ready.", "hasCode": True, "code": code, "filename": "index.html"}
    
    return {"response": f"CyberMind AI is active. Neural link processed: {req.prompt}"}

@app.post("/api/terminal")
def terminal(project: str, command: str):
    path = os.path.join(PROJECTS_ROOT, project)
    try:
        res = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=path, timeout=15)
        return {"output": res.stdout + res.stderr}
    except Exception as e:
        return {"output": str(e)}

@app.post("/api/upload")
async def upload_file(project: str, file: UploadFile = File(...)):
    p_path = os.path.join(PROJECTS_ROOT, project)
    os.makedirs(p_path, exist_ok=True)
    with open(os.path.join(p_path, file.filename), "wb") as f:
        f.write(await file.read())
    return {"status": "Success"}

# Static File Mounting
static_path = os.path.join(BASE_DIR, "static")
if os.path.exists(static_path):
    app.mount("/", StaticFiles(directory=static_path, html=True), name="static")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
