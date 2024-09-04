
from fastapi import FastAPI
import subprocess

def run_query(query: str) -> str:
    command = f'python -m graphrag.query --root ./ragtest --method global "{query}"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/query")
async def read_query(query: str):
    result = run_query(query)
    return {"result": result}
