#!/usr/bin/env python3
"""a module that contains one function 
update_topics function that updates documents
"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """
    updates all topics of a school document
    based on name given
    """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
