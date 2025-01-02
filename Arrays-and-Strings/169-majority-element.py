# Link to Leetcode problem: https://leetcode.com/problems/majority-element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Taking advantage of the definition of majority element in the question
        # The majority element occurs more than half the number of array elements
        nums.sort()
        return nums[len(nums) // 2]

        # TC: O(nlog(n))
        # SC: O(1)

        # Boyer-Moore Voting Algorithm
        '''
        result = None
        count = 0

        for num in nums:
            if count == 0:
                result = num
                count = 1
            elif num != result:
                count -= 1
            else:
                count += 1
        return result
        '''

        # TC: O(n)
        # SC: O(1)

        # Hash-map to count occurances
        '''
        counter = dict()
        maj_element = nums[0]
        maj_counter = 1

        for key in nums:
            if key in counter.keys():
                counter[key] += 1
            else:
                counter[key] = 1
            if counter[key] >= maj_counter:
                maj_counter, maj_element = counter[key], key
        
        return maj_element
        '''
        # TC: O(n)
        # SC: O(n)
