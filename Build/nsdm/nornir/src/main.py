from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Nornir API",
    description="Nornir API for executing Nornir tasks",
    version="0.1.0"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(
        app, host="127.0.0.1", 
        port=7878
        )