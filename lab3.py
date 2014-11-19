#!/usr/bin/python
#acleetus

from factor import factor
from triangle import triangle
from doubling import doubling
from factorial import factorial 
from pascal import pascal 
from occurrences import num_occurrences


print factor(60)
print factor(45)
print factor(35)
print factor(13)

triangle(3)
triangle(5)

print doubling(0.1)
print doubling(0.05)
print doubling(0.01)

print factorial(4)
print factorial(0)

pascal(10)

print num_occurrences(["a", "b", "a", "b", "c", "b", "d", "e"], "b")

