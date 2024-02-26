#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

# Count all objects
all_objects_count = storage.count()

# Count State objects
state_objects_count = storage.count(State)

# Get the first state
first_state = list(storage.all(State).values())[0]

print("All objects: {}".format(all_objects_count))
print("State objects: {}".format(state_objects_count))
print("First state: {}".format(first_state))

