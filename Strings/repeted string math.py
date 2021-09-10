from math import ceil
class Solution(object):
    def repeatedStringMatch(self, a, b):
        

        # check if b is subset from a
        # if no return -1
        if not set(b).issubset(set(a)):
            return -1
        
        s = a
        m, n = len(b), len(s)
        for i in range((m//n)+2):
			# search if b is in substring s
            if s.find(b) >= 0:
                return i+1
            s += a

        return -1
