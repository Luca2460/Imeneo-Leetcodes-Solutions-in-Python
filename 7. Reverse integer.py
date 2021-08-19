import math

def solution(x):
    rev = 0
    sign = 1
    if x < 0:
        sign = -1
        x = abs(x)
    for i in range(math.floor(math.log10(abs(x) + 0.1))+1): # x is supposed to be int, so adding 0.1 will not change the ammount of digits it has
        # pop                                          # adding an if statement for x = 0 would have worked too
        pop = x % 10
        x = int((x - pop) / 10)
        
        # push
        rev = 10*rev + pop
    return rev*sign

    # TIME complexity: O(log(N)), where N is the input integer.
    # Explaination: either as N has roughly log(N) digits or as the for cycle iterates over roughly log(x) elements

    # SPACE complexity: O(1), the number of allocated variables is constant no matter the input

x= -134
print(solution(x))