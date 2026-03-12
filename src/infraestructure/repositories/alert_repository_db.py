from sqlalchemy import select, delete
from uuid import UUID
from ...domain.entities.alert import Alert
from ...domain.interfaces.alert_repository import IAlertrepository
from ..common.services.db_utils import find_one_or_fail

class AlertrepositoryDB(IAlertrepository):
    def __init__(self, session):
        self.session = session


    async def add(self, alert: Alert) -> Alert:
        self.session.add(alert)
        await self.session.commit()
        await self.session.refresh(alert)
        return alert


    async def get_all(self) -> list[Alert]:
        result = await self.session.execute(select(Alert))
        return result.scalars().all()


    async def get_by_id(self, alert_id: UUID) -> Alert:
        result = await find_one_or_fail(
            query=select(Alert).where(Alert.id == alert_id),
            session=self.session,
            error_message=f"Alert with id {alert_id} not found."
        )
        return result

    async def delete(self, alert_id: UUID) -> None:
        await self.session.execute(delete(Alert).where(Alert.id == alert_id))
        await self.session.commit()
