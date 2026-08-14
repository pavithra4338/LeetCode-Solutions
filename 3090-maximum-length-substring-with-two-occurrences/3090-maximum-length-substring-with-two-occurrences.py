class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        left = 0
        longest = 0
        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1
            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest