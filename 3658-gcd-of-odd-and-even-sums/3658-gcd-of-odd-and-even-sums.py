class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even=0
        odd=0
        for i in range(1,n+1):
            even+=2*i
            odd+=2*i-1
        return math.gcd(even,odd)