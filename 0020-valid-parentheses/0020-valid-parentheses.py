class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=[]
        for char in s:
            if char == '(':
                st.append(')')
            elif char == '[':
                st.append(']')
            elif char == '{':
                st.append('}')
            else:
                if not st or st.pop() !=char:
                    return False
        return not st
        