# Binary search function
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the target is at mid
        if arr[mid] == target:
            return mid
        # If the target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        # If the target is smaller, ignore the right half
        else:
            right = mid - 1

    # If the target is not found, return -1
    return -1

# Main code to take user input
if __name__ == "__main__":
    try:
        # Taking input array from user
        arr = list(map(int, input("Enter the elements of the array (separated by space): ").split()))
        # Sort the array before performing binary search
        arr.sort()

        # Taking target value from user
        target = int(input("Enter the target element: "))

        # Call the binary search function
        result = binary_search(arr, target)

        # Display the result
        if result != -1:
            print(f"Element found at index: {result}")
        else:
            print("Element not found")
    except ValueError:
        print("Please enter valid integers for the array and target.")
