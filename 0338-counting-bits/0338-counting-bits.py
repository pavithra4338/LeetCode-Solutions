class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[]
        for i in range(n+1):
            num=i
            c=0
            while num>0:
                digit=num%2
                if digit==1:
                    c+=1
                num//=2
            l.append(c)
        return l