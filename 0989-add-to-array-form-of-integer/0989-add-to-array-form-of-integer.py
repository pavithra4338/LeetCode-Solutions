class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=""
        for i in num:
            n+=str(i)
        l=[]
        sum=int(n)+k
        for i in str(sum):
            l.append(int(i))
        return l