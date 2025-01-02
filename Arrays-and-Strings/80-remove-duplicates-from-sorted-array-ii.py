# Link to Leetcode problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # 2 pointers
        if len(nums) < 3:
            return len(nums)
        i = 2
        j = 2
        # i is final solution pointer
        # j is iterating pointer

        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]: # comparing current element with final solution prev-prev element (i - 2)
                nums[i] = nums[j]
                i += 1
        return i


        '''
        ptr = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[ptr] != nums[i]: # or '!='; first occurance
                ptr += 1
                nums[ptr] = nums[i]
                count = 1
            elif nums[ptr] == nums[i]:
                if count == 1: # second occurance
                    ptr += 1
                    nums[ptr] = nums[i]
                    count += 1

            return ptr
        '''

        '''
        ptr = 0
        flag = False
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                ptr += 1
                nums[ptr] = nums[i]
                flag = False
            elif nums[ptr] != nums[i]:
                ptr += 1
                nums[ptr] = nums[i]
                flag = False
            elif not flag:
                ptr += 1
                nums[ptr] = nums[i]
                flag = True
        return ptr + 1


        index = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                count += 1
                nums[index] = nums[i]
                if count <= 2:
                    index += 1
            else:
                nums[index] = nums[i]
                index += 1
                count = 1
        return index
'''