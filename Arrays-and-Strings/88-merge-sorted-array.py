# Link to Leetcode problem: https://leetcode.com/problems/merge-sorted-array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 3-pointers -> one for nums1, one for nums2 and one for solution array which is also nums1 (solving in-place)

        # starting from the last elements in nums1 and nums2
        p1 = m - 1
        p2 = n - 1

        # working backwards on the output array (nums1)
        for i in range(m + n - 1, -1, -1):
            if p1 >= 0 and p2 >= 0 and nums1[p1] >= nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            elif p2 >= 0:
                nums1[i] = nums2[p2]
                p2 -= 1
            else:
                nums1[i] = nums1[p1]
                p1 -= 1

        return nums1

        # TC: O(m + n) -> we iterate through both the arrays only once
        # SC: O(1) -> no additional space is used apart from input arrays

        # Other approaches:
        # 1. Add nums2 values at the end of nums1 and sort.
        # TC: O((m + n)log(m + n)), SC: O(1)
        '''
        del nums1[m:] # delete or replace 0 values with nums2 
        nums1.extend(nums2)
        nums1.sort()
        return nums1
        '''
        # 2. Copy nums1 to a duplicate array, 3 pointers starting from the beginning of the 3 arrays, write elements to output array in increasing order.
        # TC: O(m + n), SC: O(m)