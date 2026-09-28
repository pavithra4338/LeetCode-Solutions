class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth=0
        maxi=0
        for i in s:
            if i == "(":
                depth+=1
                if depth>maxi:
                    maxi=depth
            elif i == ")":
                depth-=1
        return maxi