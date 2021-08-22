def threeSum(nums: List[int]) -> List[List[int]]:
    sortNums = sorted(nums)
    res = []
    i = 0
    for num in sortNums:
        i += 1
        if num > 0:
            break
        if i == 1 or sortNums[i-2] != sortNums[i-1]:
            left = i
            right = len(nums) - 1
            target = -num 
            while left < right:
                diff = target - sortNums[left] - sortNums[right]
                if diff > 0:
                    left  += 1
                elif diff < 0:
                    right -= 1
                else:
                    res.append([num, sortNums[left], sortNums[right]])
                    left += 1
                    right -= 1
                    while left<right and sortNums[left] == sortNums[left-1]:
                        left += 1
    return res

    # TIME complexity O(N^2), two nested loops, sorting is O(NlogN) so it can be neglected
    # SPACE complexity Depends on the sorting