class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_freq={}
        t_freq={}
        for i in range(len(s)):
            s_ch=s[i]
            t_ch=t[i]
            if s_ch in s_freq:
                if s_freq[s_ch] != t_ch:
                    return False
            else:
                s_freq[s_ch] = t_ch
            if t_ch in t_freq:
                if t_freq[t_ch] != s_ch:
                    return False
            else:
                t_freq[t_ch] = s_ch
        return True