class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        freq = {}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in t:
            if i not in freq or freq[i] ==0:
                return i
            else:
                freq[i]-=1
       
        


        