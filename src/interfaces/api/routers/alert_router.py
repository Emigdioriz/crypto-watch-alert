from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from functools import partial
from ....application.dtos.alert_dtos import AlertReadDTO, AlertCreateDTO
from ....application.dtos.common.guid_dto import GuidResponse
from ....application.dtos.common.api_dto import ApiResponse
from ....infraestructure.repositories.alert_repository_db import AlertrepositoryDB
from ....infraestructure.config.db import Session
from ....application.use_cases.alert_use_cases import CreateAlertUseCase, GetAlertsUseCase, GetAlertByIdUseCase, DeleteAlertUseCase


router = APIRouter(prefix="/alerts", tags=["alerts"])

def get_repository(session: Session):
    return AlertrepositoryDB(session)

def get_use_case(repository: AlertrepositoryDB = Depends(get_repository), use_case_cls=None):
    return use_case_cls(repository)


@router.post(
    "/", 
    response_model=ApiResponse[GuidResponse], 
    status_code=status.HTTP_201_CREATED
)
async def create_alert(
    alert: AlertCreateDTO,
    use_case: CreateAlertUseCase = Depends(partial(get_use_case, use_case_cls=CreateAlertUseCase))
    ):
    
    alert = await use_case.execute(alert)

    return ApiResponse(detail=GuidResponse(id=alert.id))


@router.get(
    "/", 
    response_model=ApiResponse[list[AlertReadDTO]],
    status_code=status.HTTP_200_OK    
)
async def get_alerts(
    use_case: GetAlertsUseCase = Depends(partial(get_use_case, use_case_cls=GetAlertsUseCase))
):
    alerts = await use_case.execute()
    return ApiResponse(detail=alerts)


@router.get(
    '/{alert_id}',
    response_model=ApiResponse[AlertReadDTO],
    status_code=status.HTTP_200_OK
)
async def get_alert_by_id(
    alert_id: UUID,
    use_case: GetAlertByIdUseCase = Depends(partial(get_use_case, use_case_cls=GetAlertByIdUseCase))
):
    alert = await use_case.execute(alert_id)
    return ApiResponse(detail=alert)


@router.delete(
    '/{alert_id}',
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_alert(
    alert_id: UUID,
    use_case: DeleteAlertUseCase = Depends(partial(get_use_case, use_case_cls=DeleteAlertUseCase))
):
    await use_case.execute(alert_id)