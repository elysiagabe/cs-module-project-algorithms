'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers

Notes: 
-will need to iterate thru array
-need to look at slices of arr that have length k...
-only need to iterate thru to index len(arr)-k+1
-when looking at a slice, find the max value and add that to an array with the other max values
'''
# def sliding_window_max(nums, k):
#     # Your code here
#     max_values = []
#     # Iterate thru array
#     for i in range(0, len(nums)-k+1):
#         # these will be the numbers used to look at a slice of the array
#         start, end = i, i+k
#         # find the window max 
#         window_max = max(nums[start:end])
#         # add max to max_values arr
#         max_values.append(window_max)
#     # return arr
#     return max_values

'''
Second Solution: 

- the max() method is really slow when there's a large input...my first solution is OK but fails the timed portion of the large input test file
- could iterate thru the list using pointers instead...would have a var to mark the start, end, current/temp and max value...once the max is found, append to max_values array
'''

def sliding_window_max(nums, k):
    length = len(nums)
    # this will be our iterator thru the subarray we'll define with pointers (i.e., the current value we're looking at)
    curr = 0 
    end = k-1
    start = curr
    # initialize a max value
    window_max = nums[k-1]

    max_values = []

    # iterate thru subarray
    while (end <= length-1):
        # find max of subarray
        if nums[curr] > window_max:
            window_max = nums[curr]
        # incrememnt curr
        curr += 1
        
        # when you reach end of subarray, append max to max_values and shift pointers
        if end == curr and curr != length: 
            max_values.append(window_max)
            end += 1
            curr = start + 1
            start = curr

            if end < length: 
                window_max = nums[end]
    
    return max_values

'''second solution doesn't work w/large input either...perhaps there's a different data structure that's better suited for finding the max value or something?'''

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
