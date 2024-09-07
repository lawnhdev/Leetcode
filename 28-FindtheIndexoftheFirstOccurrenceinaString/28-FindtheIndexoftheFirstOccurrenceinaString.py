class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
             return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle)):
            print(haystack[i:i + len(needle)])
            if haystack[i:i + len(needle)] == needle:
                return i
        if haystack[-len(needle):] == needle:
            return len(haystack) - len(needle)
        return -1

        