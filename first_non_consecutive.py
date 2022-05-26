# Function in which we are sort out every character and find first one non-consecutive

def first_non_consecutive(arr):
    char = arr[0]
    for i in arr:
        if i != char:
            return i
        char += 1
    return None

sp = [1, 2, 3, 4, 6, 7, 8]
print(first_non_consecutive(sp))



