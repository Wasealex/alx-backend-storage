#!/usr/bin/env python3
"""a module that contains a class Cache
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


class Cache:
    def __init__(self):
        """inititailizing redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def count_calls(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            key = f"call_count:{func.__qualname__}"
            self._redis.incr(key)
            return func(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store unique id and return key"""
        key = str(uuid.uuid4())
        if isinstance(data, str):
            self._redis.set(key, data.encode("utf-8"))
        else:
            self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable[[bytes],
                                  Union[str,
                                        int,
                                        float]]] = None) -> Union[str,
                                                                  int,
                                                                  float,
                                                                  None]:
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is None:
            return data.decode("utf-8")
        else:
            return fn(data)

    def get_str(self, key: str) -> str:
        return self.get(key, None)

    def get_int(self, key: str) -> int:
        return self.get(key, int)
