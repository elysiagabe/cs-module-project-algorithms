'''
Input: an integer
Returns: an integer

Notes: 
- use recursion to keep calling eat_cookies until there are no more cookies to eat (this would signify the end of a cookie combo)
- if there are 3 or more cookies, can eat 3, 2, or 1 cookies
- if there are 2 cookies, can eat 2 or 1 cookies
- if there is 1 cookie, can only eat 1 cookie
- when there are 0 cookies, incremement the combo count
'''
def eating_cookies(n):
    # Your code here
    # initialize count variable
    count = 0
    # if there are zero cookies left, increment count
    if n == 0: 
        count += 1
        return count
    
    # if 1 cookie, call eat_cookies(n-1)
    if n == 1:
        return eating_cookies(n-1)
    # if 2 cookies, call eating_cookies(n-1) plus (n-2)
    elif n == 2:
        return eating_cookies(n-1) + eating_cookies(n-2)
    # if 3 or more cookies, call eating_cookies() on n-1, n-2 and n-3
    else: 
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
        


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
