# Function to perform linear search
def linear_search(arr, target):
    for index, value in enumerate(arr):
        # Return index if element is found
        if value == target:
            return index
    # Return -1 if element is not in the list
    return -1


# Input list and target value
numbers = [10, 23, 45, 70, 11, 15]
target_value = 70

# Search and print the result
result = linear_search(numbers, target_value)
print(result)