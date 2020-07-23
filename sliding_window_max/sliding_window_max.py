'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers

Notes: 
-will need to iterate thru array
-need to look at slices of arr that have length k...
-only need to iterate thru to index len(arr)-k+1
-when looking at a slice, find the max value and add that to an array with the other max values
'''
def sliding_window_max(nums, k):
    # Your code here
    max_values = []
    # Iterate thru array
    for i in range(0, len(nums)-k+1):
        # these will be the numbers used to look at a slice of the array
        start, end = i, i+k
        # find the window max 
        window_max = max(nums[start:end])
        # add max to max_values arr
        max_values.append(window_max)
    # return arr
    return max_values


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
