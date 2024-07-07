"""
Merge Sort Algorithm:
----------------------
Merge Sort is a divide-and-conquer algorithm that divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

Steps of Merge Sort:
1. Divide the array into two halves.
2. Recursively sort the two halves.
3. Merge the two sorted halves.

Time Complexity: O(n log n) in all cases (worst, average, and best) due to the divide and merge steps.
Space Complexity: O(n) due to the additional space used for the temporary arrays.

Python Implementation:
-----------------------
"""

def merge_sort(array):
    """
    Sorts an array in ascending order using the Merge Sort algorithm.

    Parameters:
    - array: List of elements to be sorted.
    """
    if len(array) <= 1:
        return
    
    # Find the middle point to divide the array into two halves
    middle_point = len(array) // 2
    left_part = array[:middle_point]  # Copy the left half
    right_part = array[middle_point:]  # Copy the right half

    # Recursively sort the two halves
    merge_sort(left_part)
    merge_sort(right_part)

    # Initial indexes for the left, right, and merged subarrays
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Merge the sorted halves back into the original array
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # Copy any remaining elements of the left half, if any
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    # Copy any remaining elements of the right half, if any
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    # Example usage of merge_sort
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array:')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array:', numbers)
