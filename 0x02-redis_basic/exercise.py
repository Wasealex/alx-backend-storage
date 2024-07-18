#!/usr/bin/env python3
"""a module that contains a class Cache
"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """inititailizing redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store unique id and return key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
