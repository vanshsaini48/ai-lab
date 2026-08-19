# Function to perform interpolation search
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    # Target must be within the range of elements
    while low <= high and target >= arr[low] and target <= arr[high]:
        # Handle case where low and high point to the same value
        if low == high:
            if arr[low] == target:
                return low
            return -1

        # Estimate the probe position based on value distribution
        pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))

        # Target found
        if arr[pos] == target:
            return pos

        # Target is larger, search right sub-array
        if arr[pos] < target:
            low = pos + 1
        # Target is smaller, search left sub-array
        else:
            high = pos - 1

    return -1


# Input array (must be sorted) and target value
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target_value = 70

# Search and print the result
result = interpolation_search(numbers, target_value)
print(result)