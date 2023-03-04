# stdlib
import os


class ConnectionConfig:
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", 5432)
    database = os.getenv("DB_NAME", "postgres")
    user = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASS", "postgres")


class RedisConfig:
    host = os.getenv("REDIS_HOST", "localhost")
    port = os.getenv("REDIS_PORT", 6379)
    password = os.getenv("REDIS_PASS", "redis")
    database_id = os.getenv("REDIS_DB_ID", 0)
    enabled = os.getenv("REDIS_ENABLED", "False").lower() in ("true", "1", "t")


class TTL:
    minute = 60
    hour = 60 * minute
    day = 24 * hour


class PgPoolSettings:
    """Настройки пула соединений для PostgreSQL"""

    MAX_INACTIVE_CONNECTION_LIFETIME = 200
    MIN_POOL_SIZE = 1
    MAX_POOL_SIZE = 50
