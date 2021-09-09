class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brac_map={"(": ")", "{": "}", "[": "]"}
        push=[]
        
        for ch in s:
            if len(push)==0:
                push.append(ch)
            else:
                if brac_map.get(push[-1])==ch:
                    
                    push.pop()
                else:
                    push.append(ch)
        if len(push)==0:
            return True
        return False
                
        
