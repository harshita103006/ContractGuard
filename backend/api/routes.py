from fastapi import APIRouter
from graph.workflow import graph
from api.schemas import ContractRequest
from fastapi import UploadFile, File

router = APIRouter()

@router.post("/audit")
def audit_contract(data: ContractRequest):

    result = graph.invoke(
        {
            "contract": data.contract
        }
    )

    return result

@router.post("/upload")
async def upload_contract(
    file: UploadFile = File(...)
):

    content = await file.read()

    contract = content.decode()

    result = graph.invoke(
        {
            "contract": contract
        }
    )

    return result