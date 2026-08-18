class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq={}
        for i in range(len(nums)-k+1):
            seen=set()
            for j in range(i,i+k):
                seen.add(nums[j])
            for num in seen:
                if num in freq:
                    freq[num]+=1
                else:
                    freq[num]=1
        ans=-1
        for num in freq:
            if freq[num]==1:
                ans=max(ans,num)
        return ans