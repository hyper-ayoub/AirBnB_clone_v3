#!/usr/bin/python3
""" Test .get()
"""
from models import storage
from models.state import State

nb_states = storage.count(State)
if nb_states is None:
    print("None", end="")
print("{}".format(nb_states), end="")
