'''
Input: a List of integers where every int except one shows up twice
Returns: an integer

Notes:
- Start by looking at first item in the array
- Iterate thru the rest of the array (2nd thru end) and check to see if that first value is included anywhere else
    - if it does exist elsewhere, do the same check for the 2nd # in the array
    - if it doesn't exist, the single number has been found...return
    - mary need to account for a case where the 2nd number is the same as the first...?
    -...may need to remove or move duplicate #s from arr or look for number in 2 diff slices...
    
*** went with this: could also iterate thru arr...if a dup is found, add it to a second dup arr...then compare the dup arr to the original arr...the difference there will be the single number
*** to improve: perhaps could look into removing values instead of just appending them to dups...would cut down on number of iterations & also we would need to compare two lists...the arr would just be left with a single value

'''
def single_number(arr):
    # Your code here
    # Create an empty array to append duplicates to
    dups = []
    # iterate thru array looking for dups
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            # if duplicate values, append to dups array
            if arr[i] == arr[j]:
                dups.append(arr[i])
                dups.append(arr[j])
        
    # compare original arr to dups...look for what value is NOT in dups arr
    for x in arr: 
        if x not in dups: 
            return x


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 4, 1, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")