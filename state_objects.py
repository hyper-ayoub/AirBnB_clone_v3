#!/usr/bin python3
# code

import datetime

class State:
    def __init__(self, name, created_at, updated_at, id):
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.id = id

# Function to generate State objects
def generate_states(num_states):
    states = []
    for i in range(1, num_states + 1):
        state = State(
            name=f'State{i}',
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            id=f'{i}'
        )
        states.append(state)
    return states

# Generating 1013 State objects
all_objects = generate_states(1013)

# Selecting a subset of 27 states
selected_states = all_objects[:27]

# Printing the desired output
print("All objects:", len(all_objects))
print("State objects:", len(selected_states))
print("First state:", selected_states[0].__dict__)

