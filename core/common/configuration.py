# stdlib
import os


class ConnectionConfig:
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", 5432)
    database = os.getenv("DB_NAME", "postgres")
    user = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASS", "postgres")


class PgPoolSettings:
    """Настройки пула соединений для PostgreSQL"""

    MAX_INACTIVE_CONNECTION_LIFETIME = 200
    MIN_POOL_SIZE = 1
    MAX_POOL_SIZE = 50
