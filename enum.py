
from enum import Enum
import random
import os

hello_world = "hello world"
print(hello_world)


FIGURE = Enum("FIGURE", "SQUARE TRIANGLE CIRCLE")

print(FIGURE.TRIANGLE.value)