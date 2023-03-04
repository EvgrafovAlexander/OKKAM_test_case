# stdlib
import datetime
import functools
import json
import logging
from typing import Union

# thirdparty
import aioredis
from aioredis import RedisError

# project
from common import configuration as cfg

_REDIS = None


async def get_redis():
    global _REDIS
    if not _REDIS:
        _REDIS = await aioredis.from_url(
            f"redis://{cfg.RedisConfig.host}:{cfg.RedisConfig.port}",
            password=cfg.RedisConfig.password,
            db=cfg.RedisConfig.database_id,
        )
    return _REDIS


async def get_cache(key):
    if not cfg.RedisConfig.enabled:
        return None
    try:
        redis = await get_redis()
        value = await redis.get(key)
        if value:
            value = json.loads(value)
    except RedisError as e:
        logging.exception(e)
        value = None
    return value


async def set_cache(key, value: Union[list, dict], ttl: int):
    if not cfg.RedisConfig.enabled:
        return None
    try:
        redis = await get_redis()
        if value:
            await redis.set(key, json.dumps(value, default=_default), ex=ttl)
        else:
            await redis.delete(key)
    except RedisError as e:
        logging.exception(e)


def _default(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()


def redis_cache(ttl: int):
    def decorated(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            key = _generate_key(func, *args, **kwargs)
            logging.info("key", key)
            result = await get_cache(key)
            if not result:
                result = await func(*args, **kwargs)
                await set_cache(key, result, ttl)
            return result

        return wrapped

    return decorated


def _generate_key(func, *args, **kwargs) -> str:
    return ":".join([str(":".join([func.__name__, *[str(i) for i in args], str(kwargs)]))])
