class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9*num:
            return ""
        result=""
        for i in range(num):
            if sum>=9:
                result+="9"
                sum-=9
            else:
                result+=str(sum)
                sum=0
        return result