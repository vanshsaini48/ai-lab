# Function to perform binary search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Find the middle index
        mid = (low + high) // 2

        # Target found
        if arr[mid] == target:
            return mid
        # Target is smaller, ignore right half
        elif arr[mid] > target:
            high = mid - 1
        # Target is larger, ignore left half
        else:
            low = mid + 1

    # Target not found
    return -1


# Input array (must be sorted) and target value
numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]
target_value = 55

# Search and print the result
result = binary_search(numbers, target_value)
print(result)