class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero_count = 0
        
        for i in range(len(nums)):
            if nums[i] == 0: zero_count += 1
            else: nums[i-zero_count] = nums[i]

        nums[len(nums)-zero_count:] = [0]*zero_count
        print(nums)
        # TIME complexity: O(N)
        # SPACE complexity: O(N) (have to store the input)

test = Solution()
array = [1,0,3,4,0,0,5,6]
test.moveZeroes(array)