class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        arr = []
        for ch in s:
            if ch in vowels:
                arr.append(ch)
        arr.sort()
        s = list(s)
        j = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = arr[j]
                j += 1
        return "".join(s)