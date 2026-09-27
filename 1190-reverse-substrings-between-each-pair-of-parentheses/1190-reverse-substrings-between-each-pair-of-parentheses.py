class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = []
        for ch in s:
            if ch == "(":
                s1.append(ch)
            elif ch == ")":
                temp = []
                while s1[-1] != "(":
                    temp.append(s1.pop())
                s1.pop()
                for ch in temp:
                    s1.append(ch)
            else:
                s1.append(ch)
        return "".join(s1)
