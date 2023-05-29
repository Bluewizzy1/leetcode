"""
Reverse an array in place.
"""

def reverseArray(array):
    f = array[0]
    l = array[len(array)-1]
    array[0] = l
    array[len(array)-1] = f
    return array
print(reverseArray([10, 20, 30, 40, 50]))