class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open=0
        moves=0
        for i in s:
            if i=="(":
                open+=1
            else:
                if open>0:
                    open-=1
                else:
                    moves+=1
        moves+=open
        return moves