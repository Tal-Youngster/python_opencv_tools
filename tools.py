import cv2 as cv
import numpy as np
from math import *


'''
opencv tools - functions and classes that will just make everything easier.
'''


# calculates the total distance between points
def calc_distance(point_array):
    sum = 0
    sum += [get_dis(point_array[i], point_array[i + 1]) for i in range(len(point_array) - 1)]
    return sum


# returns the distance between two points (absolute value)
def get_dis(p1,p2):
    return abs(sqrt((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2))



