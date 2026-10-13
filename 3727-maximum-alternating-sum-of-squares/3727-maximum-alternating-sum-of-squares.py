class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        ans=[]
        for num in nums:
            ans.append(num*num)
        ans.sort()
        total=0
        i=0
        j=len(ans)-1
        while i<j:
            total+=ans[j]
            total-=ans[i]
            i+=1
            j-=1
        if i==j:
            total+=ans[i]
        return total