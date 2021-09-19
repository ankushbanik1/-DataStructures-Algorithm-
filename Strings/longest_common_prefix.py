class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
       """
        l = []
        for c in zip(*strs):
            if len(set(c)) == 1:
                l.append(c[0])
            else:
                break
        return ''.join(l)
