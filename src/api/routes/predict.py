"""
Модуль, содержащий роут для предсказаний модели.
"""

from fastapi import APIRouter, BackgroundTasks

from src.models.requests import TextRequest
from src.services.model import TextToneClassifier
from src.services.utils import print_logger_info

router = APIRouter()


@router.post("/predict/")
async def predict_text_tone(
    text_request: TextRequest, background_tasks: BackgroundTasks
):
    """Predict tonality of text

    Args:
        text_request (TextRequest): text request
        background_tasks (BackgroundTasks): _description_
    """

    result = TextToneClassifier.predict_text_tone(text_request.text)
    background_tasks.add_task(
        print_logger_info,
        text_request.text,
        result,
    )
    return result
