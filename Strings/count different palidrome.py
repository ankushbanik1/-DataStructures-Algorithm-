class Solution(object):
    def countPalindromicSubsequences(self, S):
        memo = {}
        def recurs(subs):    
            if subs not in memo:
                count = 0
                for c in set(subs):
                    left, right = subs.find(c), subs.rfind(c)
                    count += 1 if left==right else 2+recurs(subs[left+1:right])
                memo[subs] = count 
            return memo[subs]
        return recurs(S) % 1000000007  
