class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        

        sequence = [False for i in s]
        sequence[-1] = s[-1] in wordDict
        true_index = []
        if sequence[-1]:
            true_index.append(len(s)-1)
        for i in range(len(s)-2, -1, -1):
            if s[i:] in wordDict:
                sequence[i] = True
                true_index.append(i)
            else :
                for k in true_index:
                    if s[i:k] in wordDict:
                        sequence[i] = True
                        true_index.append(i)
                        break
        return sequence[0]
        
        
        
        
        
        
        
        
        
#          alternative
        
       
        
        
#         n = len(s)
#         wordSet = set(wordDict)

#         def dp(start):
#             if start == n:  # Found a valid way to break words
#                 return True

#             for end in range(start + 1, n + 1):  # O(N^2)
#                 word = s[start:end]  # O(N)
#                 if word in wordSet and dp(end):
#                     return True
#             return False

#         return dp(0)


