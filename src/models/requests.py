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
