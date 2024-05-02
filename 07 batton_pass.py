"""
There are n friends standing in a line, each numbered from 1 through n inclusive.
The first one, friend 1, holds a baton. Each second, the baton is passed to next friend in line.
Once it reaches the end of the line, the direction of passing is reversed and passing continues. 
Determine who will pass and who will receive the baton at a given time.
"""

def battonPass(friends, time):
    total_passes_per_cycle = (friends - 1) * 2
    effective_time = ((time - 1) % total_passes_per_cycle) + 1

    if effective_time <= friends:
        position = effective_time
    else:
        position = 2 * friends - effective_time

    if effective_time <= friends:
        passer = position
        receiver = position + 1 if position < friends else friends
    else:
        passer = position
        receiver = position - 1 if position > 1 else 1

    return [passer, receiver]


friends = 4
time = 5

print(battonPass(friends, time))

friends = 4
time = 7

print(battonPass(friends, time))