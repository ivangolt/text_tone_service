"""
Модель для входных запросов к API
"""

from pydantic import BaseModel


class TextRequest(BaseModel):
    """
    Модель запроса для классификации эмоций по тексту.

    Attributes:
        text (str): Текст для анализа эмоций.
    """

    text: str

    class Config:
        """Model example."""

        schema_extra = {
            "example": {
                "text": "Привет, как дела? Что нового?",
            }
        }


class PredictionResult(BaseModel):
    """Модель ответа сервиса на предсказание"""

    label: str = "unknown"
    score: float = 0.0
