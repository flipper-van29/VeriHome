from fastapi import FastAPI

app = FastAPI(title="VeriHome API")

@app.get("/")
def read_root():
    return {"message": "Welcome to VeriHome API"}
