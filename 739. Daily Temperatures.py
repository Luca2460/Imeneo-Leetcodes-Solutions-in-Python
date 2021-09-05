class Solution:
    def dailyTemperatures(self, temperatures):
        stack = [0] # The stack keeps track of the temperatures that are the highest yet, in descending order.
        res = [0]*len(temperatures)
        for i in range(1, len(temperatures)):
            if temperatures[i] > temperatures[stack[-1]]:
                while stack and (temperatures[i] > temperatures[stack[-1]]): # Check the new temperature against all the temperatures in the stack
                    idx = stack.pop()
                    res[idx] = i - idx
            stack.append(i) # I only append the indexes of temperatures that are <= than the previous index
                            # and therefore, <= than all the previous indexes/elements of the stack
                            # so the last element is always the coldest of the whole stack
            # If it's not, then I take the last element of the stack and update res to put the distance/number of
            # days to be waited for that specific temperature. This will be the minimum distance as I am scanning
            # the temperatures (so moving from the closest to the farthest)
            
            # With the while loop, I keep removing from the stack all the elements that are colder than the new 
            # one and I update res, until the new element is actually colder than all the remaining ones and 
            # it will be appended on top of the stack.
        return res

        # Time complexity: O(N); for runs for ~N iterations and while can run at most for ~N iterations total, since each
        # iteration pops an element of the stack and elements are only added to the stack N times in total (this happens in the for loop)

        # Space complexity: O(N); in the worst case all the temperatures are in descending order and the whole input
        #  gets memorized in the stack.

sol = Solution()

temperatures = [70, 69, 68, 65, 69, 72, 75, 71, 67]

print(sol.dailyTemperatures(temperatures))