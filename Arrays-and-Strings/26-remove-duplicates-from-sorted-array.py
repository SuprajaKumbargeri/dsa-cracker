# Link to Leetcode problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Using 2 pointers
        i = 0
        j = 1
        # i is the final solution pointer, we keep nums[0] since it will be the first occurance of that value
        # j is the iterating pointer, starting from second element of the list

        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]: # or nums[j] != nums[i]
                i += 1
                nums[i] = nums[j]
        return i + 1

        # Additional notes:
        # taking inspiration from the previous problem,
        # we want to start storing the right elements, ignoring the wrong ones

        # These are the same approach as above but different checking conditions as mentioned:
        '''
        # Comparing the final array pointer with the iterating pointer
        ptr = 0
        for i in range(1, len(nums)):
            if nums[ptr] != nums[i]:
                ptr += 1
                nums[ptr] = nums[i]
        
        return ptr + 1

        # Comparing the iterating pointer with itself
        ptr = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                ptr += 1
                nums[ptr] = nums[i]
                
        return ptr + 1
        '''
