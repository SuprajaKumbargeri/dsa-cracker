# Link to Leetcode problem: https://leetcode.com/problems/remove-element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Filling the array correctly from front
        # Two-pointers - same direction

        i, j = 0, 0
        # i is the final solution pointer
        # j is the iterating pointer

        # write the iterating pointer value to solution if it is not equal to val
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

        # TC: O(n) - we iterate through the whole array only once
        # SC: O(1) - we do not use any additional space, modify input array in-place

        # Other approaches:
        '''
        # Removing wrong elements
        # Two Pointers - when elements to remove are rare - one fro front and one from back
        # Reduces unnecessary copy operations
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n

        # Two-pointers - opposite directions -- NOT A GOOD SOLUTION
        # False implementation -- IGNORE
        if len(nums) == 0:
            return 0
        i = 0
        j = len(nums) - 1
        while (i <= j):
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        if nums[i] == val:
            return i
        return j + 1
        '''