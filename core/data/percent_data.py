# project
from common import configuration as cfg
from common.redis import redis_cache
from readers import audiences_reader


@redis_cache(cfg.TTL.day)
async def get_percent_data(first_condition: str, second_condition: str) -> dict:
    """
    Вычисляет процент вхождения второй аудитории в первую

    :param first_condition: Условие получения первой аудитории
    :param second_condition: Условие получения второй аудитории

    :return: результат в % вхождения второй аудитории в первую
    """
    percent_data = await audiences_reader.get_percent_data(first_condition, second_condition)
    return percent_data[0]
