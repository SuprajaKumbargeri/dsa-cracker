class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        '''
        s = list(s)
        
        for start, end, direction in shifts:
            for i in range(start, end + 1):
                if direction == 1:
                    # shift forward
                    if s[i] == 'z':
                        s[i] = 'a'
                    else:
                        s[i] = chr(ord(s[i]) + 1)
                else:
                    # shift backward
                    if s[i] == 'a':
                        s[i] = 'z'
                    else:
                        s[i] = chr(ord(s[i]) - 1)
        
        return "".join(s)
    '''