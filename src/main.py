from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.interfaces.api.routers.alert_router import router as alert_router


app = FastAPI(title='alert')
app.include_router(alert_router)

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)}
    )