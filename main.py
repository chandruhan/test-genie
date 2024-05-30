from fastapi import FastAPI

app = FastAPI()


# Simple get API
@app.get("/", tags=["test-genie"])
async def root():
    return {"message": "Hello World"}