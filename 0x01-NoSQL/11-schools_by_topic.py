#!/usr/bin/env python3
"""a module that contains a function schools_by_topic
that lists topic of schools with specific topic"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    return mongo_collection.find({"topics": topic})
