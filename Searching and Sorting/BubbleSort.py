# Algorithm:

# The bubble_sort function implements the Bubble Sort algorithm to sort a given list.
# The outer loop runs n - 1 times, where n is the length of the array. This is because after each pass, the largest element "bubbles" to the end of the unsorted portion of the list.
# The inner loop compares adjacent elements and swaps them if they are in the wrong order.
# The sorting process continues until no more swaps are made, indicating that the list is sorted.
# The sorted array is returned by the bubble_sort function.
# The test list test is used as input to the bubble_sort function, and the sorted result is printed.

def bubble_sort(array):
    """Implement Bubble Sort algorithm to sort a list."""
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(bubble_sort(test))
