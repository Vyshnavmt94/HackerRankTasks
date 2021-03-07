#!/bin/python3

import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self, length, breadth):
        assert 1 <= length <= 10**3 and 1 <= breadth <= 10**3
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length * self.breadth
        return round(area, 2)

class Circle:
    def __init__(self, radius):
        assert 1 <= radius <= 10**3
        self.radius = radius

    def area(self):
        area = math.pi * self.radius**2
        return round(area, 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    assert 1 <= q <= 10**5
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        fptr.write("%.2f\n" % shape.area())
    fptr.close()
