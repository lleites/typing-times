# type: ignore

"""
Intro to Dynamic Typing

Steps
 1 - Run the code, check how dynamic types work at runtime
 2 - Remove the 'type: ignore' comment and
     see how mypy checks types at compile-time
"""

name = "Python"  # string type

name = 42  # now it is an integer

name = 3.8  # and now it is a float

name = "Guido"  # back to string

print(f"Look {name}, no static types!")
