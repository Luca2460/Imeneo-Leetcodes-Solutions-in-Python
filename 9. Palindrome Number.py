import math

def isPalindrome(x: int) -> bool: # my solution, rather slow tho
    if x < 0: return False
    num = {} # an array of ints with digNum slots would have worked too, but is tw
    digNum = math.floor(math.log10(x+0.1)) # actually this is the #of digits -1, but range starts from 0..
    for i in range(digNum + 1): # iterate through the number of digits
        pop = x % 10
        x = int(x-pop)/10
        num[i] = pop
        
    for i in range(digNum + 1):
        if num[i] != num[digNum-i]: return False
        
    return True

    # one liner solution using conversion to str: return str(x) == str(x)[::-1] (follow up asks to do without it)

    # TIME complexity: O(N) where N is the length of the number x
    # SPACE complexity: O(N)