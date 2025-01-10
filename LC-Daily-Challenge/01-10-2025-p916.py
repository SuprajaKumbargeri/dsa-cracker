# LC Link: https://leetcode.com/problems/word-subsets
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        # helper function to count the number of occurances of each letter
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        # reducing words2 to a single word
        bmax = [0] * 26
        for b in words2:
            counts = count(b)
            for i, c in enumerate(counts):
                bmax[i] = max(bmax[i], c)

        ans = []
        # compare against all words in words1
        for a in words1:
            counts = count(a)
            if all(x >= y for x, y in zip(counts, bmax)):
                ans.append(a)

        return ans
        