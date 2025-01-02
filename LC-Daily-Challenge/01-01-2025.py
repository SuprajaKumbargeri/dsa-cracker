# LC Link: https://leetcode.com/problems/maximum-score-after-splitting-a-string
class Solution:
    def maxScore(self, s: str) -> int:

        # One-pass solution
        zeros_left = 0
        ones_left = 0
        ans = -inf # not 0, total ans after adding total ones will be positive, but this partial ans can be negative

         # the substrings should be non-empty -- so divide until only the last element is left in the right sub-string
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_left += 1 # ans can be negative here and become positive after adding total ones
            else:
                ones_left += 1
            ans = max(ans, zeros_left - ones_left)
        
        # total ones
        if s[-1] == '1':
            ones_left += 1
        return ans + ones_left

        # Trick is to break-down the equation
        # Score = Zeros left + Zeros right 
        # Ones right = Ones total - Ones left
        # So, Score = Zeros left + Ones total - Ones left
        # Here Ones total is constant  and can be added to ans in the end,
        # the goal is find the combination where Zeros left - Ones left is max

        # TC: O(n)
        # SC: O(1)

        # Two-pass solution
        '''
        count_one = 0
        
        # first pass, get the count of one
        for i in range(len(s)):
            if s[i] == '1':
                count_one += 1
        
        count_zero = 0
        ans = 0
        # second pass, get counts at individual steps
        # the substrings should be non-empty -- so divide until only the last element is left in the right sub-string
        for i in range(len(s) - 1):
            if s[i] == '0':
                count_zero += 1
            else:
                count_one -= 1
                count_one = max(0, count_one)
            ans = max(ans, count_zero + count_one)

        return ans
        '''
