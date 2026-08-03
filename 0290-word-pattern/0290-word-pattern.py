class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s=s.split()
        if len(pattern) != len(s):
            return False
        pattern_freq = {}
        s_freq = {}
        for i in range(len(pattern)):
            ch = pattern[i]
            word = s[i]
            if ch in pattern_freq:
                if pattern_freq[ch] != word:
                    return False
            else:
                pattern_freq[ch] = word
            if word in s_freq:
                if s_freq[word] != ch:
                    return False
            else:
                s_freq[word] = ch
        return True
