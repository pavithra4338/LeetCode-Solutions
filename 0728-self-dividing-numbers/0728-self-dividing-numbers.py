class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l=[]
        for i in range(left,right+1):
            num = i
            valid = True
            while num > 0:
                digit = num % 10
                if digit == 0 or i % digit != 0:
                    valid = False
                    break
                num //= 10
            if valid:
                l.append(i)
        return l
