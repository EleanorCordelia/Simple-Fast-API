import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from Eleanor Cordelia - 18222059!"}   

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)