import collections
import re
import itertools

from typing import Any, Dict, Tuple, List


from web.common import postgres_connector


def __format_sql(sql: str):
    """:name -> %(name)s"""
    sql = re.sub(r"(:[a-zA-Z_0-9]+)", r"%(\1)s", sql)
    return sql.replace(":", "")


def format_to_pg_sql(query: str, named_args: Dict[str, Any]) -> Tuple[str, List[Any]]:
    """
    query = "select * from user where name = :name and email = :email"
    named_args = {'name': 'John Cena', 'email': 'cena@example.org'}
    ->
    formatted_query - select * from user where name = $1 and email = $2
    positional_args - ['John Cena', 'cena@example.org']
    """
    query = __format_sql(query)

    positional_generator = itertools.count(1)
    positional_map = collections.defaultdict(lambda: "${}".format(next(positional_generator)))
    formatted_query = query % positional_map
    positional_items = sorted(
       positional_map.items(),
        key=lambda item: int(item[1].replace("$", "")),
    )
    positional_args = [named_args[named_arg] for named_arg, _ in positional_items]

    return formatted_query, positional_args


async def get_data(sql: str, params: dict):
    query, positional_args = format_to_pg_sql(sql, params)

    pool = await postgres_connector.get_pool()
    if not pool:
        return []
    async with pool.acquire() as conn:
        await conn.set_type_codec(
            "numeric", encoder=str, decoder=float, schema="pg_catalog", format="text"
        )
        records = await conn.fetch(query, *positional_args)
        return [dict(record) for record in records]
