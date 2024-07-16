#!/usr/bin/env python3
"""Module that contains a func"""


import pymongo


def list_all(mongo_collection):
    """lists all documents in a collection"""
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [doc for doc in docs]
