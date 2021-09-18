class Solution(object):
    def strStr(self, haystack, needle):
        
        if needle!="":
            return haystack.index(needle) if needle in haystack else -1
        else:
            return 0
        
