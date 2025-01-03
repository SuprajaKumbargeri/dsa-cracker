# LC Link:https://leetcode.com/problems/number-of-ways-to-split-array
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        # Using constant space - no prefix sum array
        # it is still a 2 pass solution
        right_sum = sum(nums) # this is total sum or prefix_sum[-1]
        left_sum = 0
        res = 0

        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if left_sum >= right_sum:
                res += 1

        return res

        # TC: O(n)
        # SC: O(1)

        # Using prefix sum array
        '''
        # takes 2 passes
        sum = 0
        prefix_sum = []
        for num in nums:
            sum += num
            prefix_sum.append(sum)

        # checking for valid splits until the last but one element since there is always atleast one element in the right split
        res = 0
        for i in range(len(nums) - 1):
            left_sum = prefix_sum[i]
            right_sum = prefix_sum[-1] - prefix_sum[i]
            if left_sum >= right_sum:
                res += 1
        
        return res

        # TC: O(n)
        # SC: O(n)
        '''