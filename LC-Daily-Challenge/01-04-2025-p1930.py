# LC Link: https://leetcode.com/problems/unique-length-3-palindromic-subsequences
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        res = 0

        # the outer loop runs in constant time since there are only 26 letters
        for letter in letters:
            # index() and rindex() take constant time
            i, j = s.index(letter), s.rindex(letter)
            if i < j:
                # This takes O(n) TC
                res += len(set(s[i + 1 : j]))
        return res

        # TC: O(26n)=O(n)
        # SC: O(1)
        
        # I implemented this elaborate solution which takes advantage that only 26 letters exist. However, there was a critical flaw in my code especially in the line `first_index[i] < last_index[j] and last_index[i] > first_index[j]`
        # Incorrect -- Ignore
        '''
        first_index = [-1] * 26
        last_index = [-1] * 26
        count = [0] * 26

        for i in range(len(s)):
            letter = ord(s[i]) - ord('a')
            count[letter] += 1
            if first_index[letter] == -1:
                first_index[letter] = i
            last_index[letter] = i

        res = 0
        ans = []
        for i in range(26):
            if count[i] < 2:
                # the first char did not appear atleast 2 times, it cannot be part of pali
                continue
            for j in range(26):
                if count[j] < 1:
                    continue
                if i == j:
                    # checking for the same first and second chars
                    if count[i] >= 3:
                        res += 1
                else:
                    # checking for different first and second chars
                    if first_index[i] < last_index[j] and last_index[i] > first_index[j]:
                        res += 1
        return res
        '''