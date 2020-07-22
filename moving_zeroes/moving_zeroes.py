'''
Input: a List of integers
Returns: a List of integers

Notes: 
- want to move zeroes to end of array
- iterate thru the array...if value at index is 0, then remove it from the array, then append to the end <=== This mostly works but if array is front-loaded with zeroes (e.g., test file test starting at line 48), this won't work....need to also move integers to the front
- could try swtiching...but that would probably require multiple pass thrus 
'''
def moving_zeroes(arr):
    # Your code here
    # Iterate thru array
    for i in range(0, len(arr)):
        # if item is 0, 
        if arr[i] == 0:
            # remove item from array and add it to the end
            arr.append(arr.pop(i))
        # otherwise,
        else:
            # remove item from array and insert it at the beginning
            arr.insert(0, arr.pop(i))
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")