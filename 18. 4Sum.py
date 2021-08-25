# came up with it myself. However, it turns out that in the solutions they're expecting you to find a generic k-sum, which sounds a bit hard
def fourSum(nums, target): 
    l = len(nums) - 1
    if l < 3:
        return
    
    nums = sorted(nums)
    res = []
    
    for i in range(l-2):
        if i == 0 or nums[i] != nums[i-1]:
            if nums[i] > target and nums[i] >= 0:
                return res
            targ = target - nums[i]
            
            for j in range(i+1, l-1):
                
                if j == i+1 or nums[j] != nums[j-1]:
                    if nums[j] < targ or nums[j] <= 0:
                        t = targ - nums[j]
                        lo = j+1
                        hi = l

                        while hi>lo:
                            s = nums[lo] + nums[hi]
                            if s > t:
                                hi -= 1
                            elif s < t:
                                lo += 1
                            else:
                                res.append([nums[i], nums[j], nums[lo], nums[hi]])
                                lo += 1
                                hi -= 1
                                while nums[lo] == nums[lo-1] and hi>lo:
                                    lo += 1
    return res

    # TIME complexity: O(N^3)
    # SPACE complexity: O(N) for the sorting
n = [1,0,-1,0,-2,2]
print(fourSum(n, 0)) 