"""
Модуль, содержащий логику работы с моделью машинного обучения.

"""

from torch import set_num_threads
from transformers import pipeline

set_num_threads(1)
# устанавливаем количество потоков


class TextToneClassifier:
    """Classificator of text tonality based pre-trained model Transformers from Hugging Faces

    Returns:
        _type_: returns metric
    """

    model = pipeline(model="seara/rubert-tiny2-ru-go-emotions")

    @classmethod
    def predict_text_tone(cls, text: str):
        """predict text tonality

        Args:
            text (str): _description_
        """
        result = cls.model(text)
        return result
