# LC Link: https://leetcode.com/problems/jump-game
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # greedy
        max_jump_index = 0
        for i in range(len(nums)):
            if i <= max_jump_index:
                curr_jump = i + nums[i]
                max_jump_index = max(max_jump_index, curr_jump)
                if max_jump_index >= len(nums) - 1:
                    return True
            else:
                return False
        return False

        # TC: O(n)
        # SC: O(1)

        # Other approaches:
        # - Top-up DP using memo table and recursion
        # - Botton-down DP using memo table and iteration
        # For both methods, TC: O(n^2) and SC: O(n)

        # Previous implementation - same as greedy
        '''
        max_jump_index = 0
        for i in range(len(nums)):
            if i != len(nums) - 1: # do not check for last index, check for other indices
                max_jump_index = max(max_jump_index, i + nums[i])

            if max_jump_index >= (len(nums) - 1): # return True if we can reach the last index
                return True

            if max_jump_index == i: # return False if we cannot jump any further from the current index
                return False
        
        return False
        '''
