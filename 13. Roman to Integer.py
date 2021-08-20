def romanToInt(s: str) -> int:

    # note: len(s) <= 15

    out = 0
    symbols = {'M':1000, 'CM':900,
                'D':500, 'CD':400,
                'C':100, 'XC':90,
                'L':50, 'XL':40, 
                'X':10, 'IX': 9,
                'V':5, 'IV':4,
                'I':1}
    while len(s) != 0:
        if s[-2:] in symbols:
            out = out + symbols[s[-2:]]
            s = s[:-2]
        else:
            out = out + symbols[s[-1]]
            s = s[:-1]
            
    return out

    # TIME complexity: O(N), where N is the length of the string (One might also say O(1) since the maximum cost is known and constant)
    # SPACE complexity: O(1)