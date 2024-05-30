from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["test-genie"])
async def root():
    return {"message": "Hello World"}