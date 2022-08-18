# https://www.hackerrank.com/challenges/30-arrays/problem?h_r=profile
# return the reverse of a list in the form of space separated integers

# with reverse function
def list_reverse(arr):
    arr.reverse()
    for i in arr:
        print(i, end=" ")

print(list_reverse([1,2,3,4,5]))




