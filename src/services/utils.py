"""
Вспомогательные утилиты, используемые в сервисе

"""

from datetime import datetime

from loguru import logger


async def print_logger_info(input_text: str, predicted):
    """
    printintng logger
    """

    logger.info({"input_text": input_text, "predicted": predicted})


def return_current_time():
    """function return current time"""
    return datetime.utcnow().isoformat()
