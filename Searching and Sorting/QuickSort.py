"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

# Algorithm:
# The quicksort function implements the Quick Sort algorithm to sort a given list.
# If the length of the array is less than or equal to 1, it means the list is already sorted, so the function returns the array as it is.
# Otherwise, the first element of the array is chosen as the pivot.
# Two separate lists, lesser and greater, are created to hold elements that are less than or equal to the pivot and elements that are greater than the pivot, respectively.
# Using list comprehensions, elements from array[1:] are iterated. If an element is less than or equal to the pivot, it is added to the lesser list; otherwise, it is added to the greater list.
# Recursively, the quicksort function is called on the lesser list and the greater list, and the sorted results are concatenated with the pivot element in between.
# The final sorted list is returned.
# The test list test is used as input to the quicksort function, and the sorted result is printed.


def quicksort(array):
    """Implement Quick Sort algorithm to sort a list."""
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]  # Choose the first element as the pivot
        lesser = [x for x in array[1:] if x <= pivot]  # Elements less than or equal to the pivot
        greater = [x for x in array[1:] if x > pivot]  # Elements greater than the pivot
        return quicksort(lesser) + [pivot] + quicksort(greater)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
