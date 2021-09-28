class Solution:
    def maxSubArray(self, nums: List[int]) -> int: # had to look up the solutions for this
        maximum = nums[0]
        curr_subarray = nums[0]
        
        for num in nums[1:]:
            curr_subarray = max(num, curr_subarray + num) 
            # at each iteration we check whether the old part of the subarray is actually helpful and wotth keeping
            # If it's not, we'll dump it, as it won't be helpful for any other subarray
            if curr_subarray > maximum: maximum = curr_subarray
            # We could store a i index if the question asked for it
        return maximum
        # TIME complexity: O(N)
        # SPACE complexity: O(1)
        