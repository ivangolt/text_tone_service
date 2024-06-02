"""
Основной маршрутизатор, который объединяет все маршруты API

"""

from fastapi import APIRouter

from src.api.routes import healthcheck, predict

router = APIRouter()

router.include_router(predict.router, tags=["predict"])
router.include_router(healthcheck.router, tags=["healthcheck"])
