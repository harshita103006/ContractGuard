from fastapi import APIRouter
from graph.workflow import graph
from api.schemas import ContractRequest

router = APIRouter()

@router.post("/audit")
def audit_contract(data: ContractRequest):

    result = graph.invoke(
        {
            "contract": data.contract
        }
    )

    return result