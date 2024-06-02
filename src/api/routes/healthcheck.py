"""
Модуль, содержащий роут для проверки состояния сервиса.

"""

from fastapi import APIRouter

from src.models.healthcheck import HealthcheckResult
from src.services.utils import return_current_time

router = APIRouter()


@router.get("/healthcheck/", response_model=HealthcheckResult, name="healthcheck")
async def get_health_check() -> HealthcheckResult:
    """Healthcheck endpoint"""
    health_check = HealthcheckResult(is_alive=True, date=return_current_time())

    return health_check
