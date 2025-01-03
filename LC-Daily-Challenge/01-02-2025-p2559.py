# LC Link: https://leetcode.com/problems/count-vowel-strings-in-ranges
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        # helper function to check if a char is vowel or not
        def isVowel(c: str):
            if c in {'a', 'e', 'i', 'o', 'u'}:
                return True
            return False

        prefix_sum = []
        sum = 0
        # processing words to a list of boolean checking if the strings start and end with a vowel and storing them into a prefix sum array
        for s in words:
            if isVowel(s[0]) and isVowel(s[-1]):
                sum += 1
            prefix_sum.append(sum)

        ans = []
        for l, r in queries:
            prev_l_prefix_sum = 0 if l == 0 else prefix_sum[l - 1]
            r_prefix_sum = prefix_sum[r]
            ans.append(r_prefix_sum - prev_l_prefix_sum)
        
        return ans

        # m is length of words and n is length of queries
        # TC: O(m + n)
        # SC: O(m) -> ignoring output array