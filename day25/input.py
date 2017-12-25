# Begin in state A.
# Perform a diagnostic checksum after 6 steps.
#
# In state A:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state B.
#   If the current value is 1:
#     - Write the value 0.
#     - Move one slot to the left.
#     - Continue with state B.
#
# In state B:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state A.
#   If the current value is 1:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state A.

states_example = {
    'a': {
        'write': [1, 0],
        'move': [1, -1],
        'next': ['b', 'b'],
    },
    'b': {
        'write': [1, 1],
        'move': [-1, 1],
        'next': ['a', 'a'],
    },
}

states = {
  'a': {
    'write': [1, 0],
    'move': [1, 1],
    'next': ['b', 'f'],
  },
  'b': {
    'write': [0, 1],
    'move': [-1, -1],
    'next': ['b', 'c'],
  },
  'c': {
    'write': [1, 0],
    'move': [-1, 1],
    'next': ['d', 'c'],
  },
  'd': {
    'write': [1, 1],
    'move': [-1, 1],
    'next': ['e', 'a'],
  },
  'e': {
    'write': [1, 0],
    'move': [-1, -1],
    'next': ['f', 'd'],
  },
  'f': {
    'write': [1, 0],
    'move': [1, -1],
    'next': ['a', 'e'],
  },
}