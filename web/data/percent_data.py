# stdlib
from typing import List

# project
from web.readers import audiences_reader


async def get_percent_data(first_condition: str, second_condition: str) -> List[dict]:
    """
    Вычисляет процент вхождения второй аудитории в первую

    :param first_condition: Условие получения первой аудитории
    :param second_condition: Условие получения второй аудитории

    :return: % вхождения второй аудитории в первую
    """
    return await audiences_reader.get_percent_data(first_condition, second_condition)
