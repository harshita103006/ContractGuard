from fastapi import FastAPI

app = FastAPI(
    title="ContractGuard API"
)

@app.get("/")
def home():
    return {
        "message": "ContractGuard Running"
    }