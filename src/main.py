
from fastapi import FastAPI
import subprocess

def run_query(query: str) -> str:
    command = f'python -m graphrag.query --root ./ragtest --method local "{query}"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

# say a hello world message text response at root
@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/query")
async def read_query(query: str):
    result = run_query(query)
    return {"result": result}
