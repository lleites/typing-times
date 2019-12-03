# Typing times
A humble introduction to type hinting in Python with Mypy
## Intro
 Python is a strongly, dynamically typed language

Strong typing means that the type of a value doesn't change in unexpected ways. Every change of type requires an explicit action.

Dynamic typing means that runtime objects (values) have a type, as opposed to static typing where variables have a type.

Type hints and tools like [Mypy](http://mypy-lang.org/) help us to make Python a statically typed language at *compile-time*

At *run-time* Python is still dynamically typed

*Source: https://stackoverflow.com/questions/11328920/is-python-strongly-typed*

## Tutorial
This is a basic introduction to how Python type hints and Mypy work

The files are meant to be open in alphabetical order and follow the steps that you can read on the top of the file.

Please open this files with Visual Code and with the mypy plugin enabled: 
`python.linting.mypyEnabled = true`


### Table of contents:
0. [Intro to Dynamic Typing](intro_dynamic_typing.py)
0. [Finding problems at run-time](t0_no_hints.py)
0. [Adding type hints for parameters only](t1_parameter_hints.py)
0. [Adding type hints for return value](t2_hints_everywhere.py)
0. [Making function result Optional](t3_invalid_parameters.py)
0. [Using dataclasses](t4_dataclasses.py)