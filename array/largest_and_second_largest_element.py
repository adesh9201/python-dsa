def find_largest_and_second_largest(arr):
    n = len(arr)

    # Check if array has at least two elements
    if n < 2:
        print("Array must contain at least two elements.")
        return None, None

    # Initialize largest and second largest
    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        print("There is no second largest element (all elements are equal).")
        return largest, None

    return largest, second_largest


# Example usage
arr = [12, 35, 1, 10, 34, 1]
largest, second_largest = find_largest_and_second_largest(arr)

print("Largest element:", largest)
print("Second largest element:", second_largest)