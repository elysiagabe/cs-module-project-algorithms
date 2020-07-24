'''
Input: a List of integers
Returns: a List of integers

Notes: 
- first idea: loop thru the array...for each item in the array, create a list that does NOT include that item (that list will only include the numbers you want to multiply together)....multiply each item in the new list...that'll be the product....then replace the item in the array w/the product
- actually w/ the above solution, need to store the value in a new products array (otherwise, for example, for the second value in the array, it'll use the new product to multiply with the other numebrs)
- issue: I'm currently filtering out the value of arr[i]....if the list has duplicate values,  this will NOT work (fails test)
- instead of above: loop thru the array...for each item, find the product of all items to the left and the product of all items to the right....then multiply these together....then add this to a products array...

- can i make this so there aren't nested for loops? 
'''
def product_of_all_other_numbers(arr):
    # Your code here

    products = [0] * len(arr)

    for i in range(0, len(arr)):
        product = left_product = right_product = 1

        for n in arr[:i]:
            left_product = left_product * n
        
        for n in arr[i+1:]:
            right_product = right_product * n
        
        product = right_product * left_product

        products[i] = product
    
    return products


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
