# thirdparty
import asyncpg

_CONNECTION_POOL = None


async def get_pool():
    """Получение пула соединений"""
    global _CONNECTION_POOL

    if not _CONNECTION_POOL:
        _CONNECTION_POOL = await asyncpg.create_pool(
            user="postgres",
            password="postgres",
            database="postgres",
            host="0.0.0.0",
            port=5438,
            max_inactive_connection_lifetime=200,
            min_size=1,
            max_size=50,
        )
    return _CONNECTION_POOL
