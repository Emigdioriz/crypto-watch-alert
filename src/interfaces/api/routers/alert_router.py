from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from ....application.dtos.alert_dtos import AlertRead, AlertCreateDTO
from ....application.dtos.common.guid_dto import GuidResponse
from ....application.dtos.common.api_dto import ApiResponse
from ....infraestructure.repositories.alert_repository_db import AlertrepositoryDB
from ....infraestructure.config.db import Session
from ....application.use_cases.create_alert import CreateAlertUseCase



router = APIRouter(prefix="/alerts", tags=["alerts"])

# TODO refatorar para um função get_repository mais genérica, para evitar repetir o código de injeção de dependência em cada rota
def get_repository(session: Session):
    return AlertrepositoryDB(session)

def get_create_alert_use_case(repository: AlertrepositoryDB = Depends(get_repository)):
    return CreateAlertUseCase(repository)


@router.post(
    "/", 
    response_model=ApiResponse[GuidResponse], 
    status_code=status.HTTP_201_CREATED
)
async def create_alert(
    alert: AlertCreateDTO,
    use_case: CreateAlertUseCase = Depends(get_create_alert_use_case)
    ):
    
    alert = await use_case.execute(alert)

    return ApiResponse(detail=GuidResponse(id=alert.id))