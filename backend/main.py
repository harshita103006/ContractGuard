from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="ContractGuard API"
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "ContractGuard Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }