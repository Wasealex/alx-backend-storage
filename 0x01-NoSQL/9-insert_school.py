#!/usr/bin/env python3
"""Module that contains one function insert_school that returns inserts new docs in a collection"""


import pymongo


def insert_school(mongo_collection, **kwargs):
    """inserts a new documents in a collection using many key/value pairs"""
    return mongo_collection.insert(kwargs)
