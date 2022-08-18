# https://www.hackerrank.com/challenges/30-arrays/problem?h_r=profile
# return the reverse of a list in the form of space separated integers

def rev_list(arr):
    arr.reverse()
    for i in arr:
        print(i, end=" ")

print(rev_list([1,2,3,4,5]))

