class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        total = 0
        for i in range(len(arr)):
            current_sum = 0
            for j in range(i, len(arr)):
                current_sum += arr[j]
                if (j - i + 1) % 2 == 1:
                    total += current_sum
        return total