# project
from web.common import db_common


async def get_percent_data(first_condition: str, second_condition: str):
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
    select 100 * sum(avg_weight_2) / sum(avg_weight_1) as percent
    from group_1
    left join group_2 on group_2.respondent = group_1.respondent
    """
    params = {}
    return await db_common.get_data(sql, params)
