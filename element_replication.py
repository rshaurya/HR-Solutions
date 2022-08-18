
# take a list and print each of its elements s times

def element_rep(arr, s):
    for i in range(0, len(arr)):
        a = arr[i] * s
        for j in a:
            print(j)

print(element_rep(['1','2'], 4))
