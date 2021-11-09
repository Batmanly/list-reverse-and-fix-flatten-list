array = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_array(array):
    array.reverse()
    for i in range(len(array)):
        array[i].reverse()
    return array

print(reverse_array(array))