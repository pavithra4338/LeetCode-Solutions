class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.lower()
        c=0
        for i in range(1,len(s)):
            if s[i-1] != s[i]:
                c+=1
        return c