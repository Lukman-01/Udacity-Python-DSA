# Algorithm:
# The merge_sort function implements the Merge Sort algorithm to sort a given list.
# If the length of the array is less than or equal to 1, it means the list is already sorted, so the function returns the array as it is.
# Otherwise, the array is split into two halves: left_half and right_half. The middle index is calculated using integer division.
# Recursive calls to merge_sort are made on the left_half and right_half lists to sort them.
# The sorted halves are then merged together using the merge function.
# The merge function takes two sorted lists (left and right) and merges them into one sorted list.
# The merging process compares elements from the left and right lists and appends the smaller element to the merged list.
# Once one of the lists is exhausted, the remaining elements from the other list are appended to the merged list.
# The sorted merged list is returned.
# The test list test is used as input to the merge_sort function, and the sorted result is printed.

def merge_sort(array):
    """Implement Merge Sort algorithm to sort a list."""
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    """Merge two sorted lists into one sorted list."""
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements, if any
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(merge_sort(test))
