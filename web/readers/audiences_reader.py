from web.common import db_common


async def get_percent_data(first_condition: str, second_condition: str):
    sql = f"""
        select au.date,
            au.respondent,
            au.sex,
            au.age,
            au.weight
        from audiences au
        where ({first_condition}) or ({second_condition})
    """
    params = {}
    res = await db_common.get_data(sql, params)
    return res
