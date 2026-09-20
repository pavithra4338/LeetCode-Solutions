class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp=26
        freq={}
        for i in "abcdefghijklmnopqrstuvwxyz":
            freq[i]=temp
            temp-=1
        n=0
        for i,ele in enumerate(s):
            n+=(freq[ele]*(i+1))
        return n