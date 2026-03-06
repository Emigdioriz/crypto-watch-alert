from fastapi import FastAPI
from src.interfaces.api.routers.alert_router import router as alert_router


app = FastAPI(title='alert')
app.include_router(alert_router)