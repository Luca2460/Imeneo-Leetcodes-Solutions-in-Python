def twoSum(self, numbers: List[int], target: int) -> List[int]: # I came up with it myself
    i = 0
    j = len(numbers) - 1
    
    for k in range(len(numbers) - 1):
        diff = numbers[i] + numbers[j] - target
        if diff == 0:
            return [i+1, j+1]
        if diff > 0:
            j = j -1
        else:  # I used elif diff < 0, solutions used just else which did improve speed
            i = i + 1
    
    # TIME complexity: O(N), where N is the length of the list, as we do a single pass over the list using the for cycle
    # SPACE complexity: O(1)