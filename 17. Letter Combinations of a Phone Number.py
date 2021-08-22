def letterCombinations(digits: str) -> List[str]:
    if len(digits) == 0:
        return []
    
    letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"} # strings "abc" are iterable 
    
    def backtrack(i, path):
        if len(path) == len(digits):
            res.append("".join(path))
            return
    
        for letter in letters[digits[i]]:
            path.append(letter)
            backtrack(i+1, path)
            path.pop() # only 1 path is kept in memory at any given time!
    
    res = []
    backtrack(0,[])
    return res

    # TIME complexity O(N*4^N), where N is the length of digits. There are 4^N possible combinations and each costs up to N to build
    # SPACE complexity O(N) or O(N*4^N) considering the space of the output. Each path requires O(N) space to be built
    # and we put 4^N of them in the output