def maxArea(height: List[int]) -> int: # had to read the solution to get the intuition; I implemented it myself
    maxArea = 0
    left = 0
    right = len(height) - 1
    for i in range(len(height) - 1):
        maxArea = max(maxArea, (right-left)*min(height[right], height[left]) )
        if height[right]>height[left] :
            left = left + 1
        else:
            right = right - 1
    return maxArea

    # TIME complexity: O(N), because of the for cycle over the length of the list
    # SPACE complexity: O(1)