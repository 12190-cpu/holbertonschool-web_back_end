#!/usr/bin/env python3
"""Module that returns schools matching a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """Return the list of schools having a specific topic."""
    return list(mongo_collection.find({"topics": topic}))
