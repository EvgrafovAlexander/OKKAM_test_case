# thirdparty
import asyncpg

# project
from common import configuration as cfg

_CONNECTION_POOL = None


async def get_pool():
    """Получение пула соединений"""
    global _CONNECTION_POOL

    if not _CONNECTION_POOL:
        _CONNECTION_POOL = await asyncpg.create_pool(
            user=cfg.ConnectionConfig.user,
            password=cfg.ConnectionConfig.password,
            database=cfg.ConnectionConfig.database,
            host=cfg.ConnectionConfig.host,
            port=cfg.ConnectionConfig.port,
            max_inactive_connection_lifetime=cfg.PgPoolSettings.MAX_INACTIVE_CONNECTION_LIFETIME,
            min_size=cfg.PgPoolSettings.MIN_POOL_SIZE,
            max_size=cfg.PgPoolSettings.MAX_POOL_SIZE,
        )
    return _CONNECTION_POOL
