# ✅ Method 1: In-place reversal using two pointers


def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap elements at left and right
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


# Example usage
arr = [1, 2, 3, 4, 5]
print("Original array:", arr)
reversed_arr = reverse_array(arr)
print("Reversed array:", reversed_arr)









# Method 2: Using Python slicing (not in-place if you create new array)

def reverse_array(arr):
    return arr[::-1]


# Example usage
arr = [1, 2, 3, 4, 5]
print("Original array:", arr)
print("Reversed array:", reverse_array(arr)) 