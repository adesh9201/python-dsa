def is_sorted(arr):
    n = len(arr)

    # Edge case: empty or single element array is considered sorted
    if n == 0 or n == 1:
        return True

    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False

    return True


# Example usage
arr = [1, 2, 3, 4, 5]
print("Is array sorted?", is_sorted(arr))  # Output: True

arr2 = [10, 5, 20]
print("Is array sorted?", is_sorted(arr2))  # Output: False