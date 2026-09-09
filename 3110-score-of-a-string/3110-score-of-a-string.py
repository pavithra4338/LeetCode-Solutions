class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        score=0
        for i in range(len(s)-1):
            a=s[i]
            b=s[i+1]
            ascc=abs(ord(a)-ord(b))
            score+=ascc
        return score