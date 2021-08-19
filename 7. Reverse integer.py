import math

def solution(x):
    rev = 0
    for i in range(math.floor(math.log10(x + 0.1))+1): # x is supposed to be int, so adding 0.1 will not change the ammount of digits it has
        # pop                                          # adding an if statement for x = 0 would have worked too
        pop = x % 10
        x = int((x - pop) / 10)
        
        # push
        rev = 10*rev + pop
    return rev

x= 134
print(solution(x))