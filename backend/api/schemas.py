from pydantic import BaseModel

class ContractRequest(BaseModel):
    contract: str