def intToRoman(num: int) -> str: 
    sol = ""
    
    # We know that 1<=num<=3999
    # I proceed with taking care of thousands, hundreds, tens and ones
    # This is a bit hardcoded.

    # thousands
    pop = num % 1000
    temp = int((num-pop)/1000)
    sol = sol + temp*"M"
    num = pop
    
    # hundreds
    pop = num % 100
    temp = int((num-pop)/100)
    num = pop
    if temp == 9:
        sol = sol + "CM"
    elif temp < 9 and temp >= 5:
        sol = sol + "D" + "C"*(temp-5)
    elif temp == 4:
        sol = sol + "CD"
    elif temp < 4:
        sol = sol + "C"*temp
        
    # tens
    pop = num % 10
    temp = int((num-pop)/10)
    num = pop
    if temp == 9:
        sol = sol + "XC"
    elif temp < 9 and temp >= 5:
        sol = sol + "L" + "X"*(temp-5)
    elif temp == 4:
        sol = sol + "XL"
    elif temp < 4:
        sol = sol + "X"*temp
        
    # units 
    temp = num
    if temp == 9:
        sol = sol + "IX"
    elif temp < 9 and temp >= 5:
        sol = sol + "V" + "I"*(temp-5)
    elif temp == 4:
        sol = sol + "IV"
    elif temp < 4:
        sol = sol + "I"*temp
        
    return sol