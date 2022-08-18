# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_r=profile
# program to rotate a list to the left a number of times given by user
# a is the array
# d is number of rotations

def rotLeft(a, d):
    l = a[d:] + a[:d]
    return l

print(rotLeft([1,2,3,4,5], 4))