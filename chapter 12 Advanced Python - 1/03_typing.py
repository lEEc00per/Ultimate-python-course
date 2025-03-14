from typing import List as l
from typing import Dict as d
from typing import Union as u
from typing import Tuple as t

# List of numbers
numbers: l[int] = [1, 2, 3, 4, 5]

# Dictionary with strings and integers
scores: d[str, int] = {"junaid": 17, "harry": 34}

# Tuple of a string and integers
person: t[str, int] = ("junaid", 17)

# Union type for variables that can hold multiple types
identifier: u[str, int] = "ID123"
identifier = "ID123" # Also valid