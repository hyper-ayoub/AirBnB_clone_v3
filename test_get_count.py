#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

# Count all objects
print("All objects: {}".format(storage.count()))

# Count State objects
print("State objects: {}".format(storage.count(State)))

# Get all State objects
all_states = list(storage.all(State).values())

if all_states:
    # If there are State objects, get the first state's ID
    first_state_id = all_states[0].id
    print("First state: {}".format(storage.get(State, first_state_id)))
else:
    print("No State objects found.")

