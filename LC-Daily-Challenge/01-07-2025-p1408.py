class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        # Brute force
        '''
        res = []
        for a in range(len(words)):
            for b in range(len(words)):
                if a != b and len(words[a]) <= len(words[b]):
                    # checking if words[a] is a substring of words[b]
                    if words[a] in words[b]:
                        res.append(words[a])
        return res
        '''
        # TC: O(m^2 * n^2)
        # SC: O(1)
