# thirdparty
import asyncpg

_CONNECTION_POOL = None


async def get_pool():
    global _CONNECTION_POOL

    if not _CONNECTION_POOL:
        _CONNECTION_POOL = await asyncpg.create_pool(
            user="postgres",
            password="postgres",
            database="postgres",
            host="localhost",
            port=5438
            # max_inactive_connection_lifetime
            # max_size
        )
    return _CONNECTION_POOL
