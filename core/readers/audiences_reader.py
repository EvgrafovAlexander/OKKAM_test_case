# stdlib
from typing import List

# project
from common import db_common


async def get_percent_data(first_condition: str, second_condition: str) -> List[dict]:
    """
    Вычисляет процент вхождения второй аудитории в первую

    :param first_condition: Условие получения первой аудитории
    :param second_condition: Условие получения второй аудитории

    1) Выделяется перечень респондентов для каждой из аудиторий,
    вычисляется их средний вес;
    2) Вычисляется процент вхождения второй аудитории в первую

    :return: % вхождения второй аудитории в первую
    """
    sql = f"""
    with group_1 as (
        select a.respondent,
            avg(a.weight) as avg_weight_1
        from audiences a
        where {first_condition}
        group by respondent
    ),
    group_2 as (
        select a.respondent,
            avg(a.weight) as avg_weight_2
        from audiences a
        where {second_condition}
        group by respondent
    )
    select
        case
            when sum(avg_weight_1) is null then 100.0
            when sum(avg_weight_2) is null then 0.0
            else 100 * sum(avg_weight_2) / sum(avg_weight_1)
        end percent
    from group_1
    left join group_2 on group_2.respondent = group_1.respondent
    """
    params = {}
    return await db_common.get_data(sql, params)
