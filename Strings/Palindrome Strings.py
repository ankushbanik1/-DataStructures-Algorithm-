class Solution:
	def isPlaindrome(self, S):
		# code here
		
		i=0
		
		n=len(S)-1
		
		while(i<n):
		    if S[i]!=S[n]:
		        return 0
		    
	
		    i+=1
		    n-=1
		        
		return 1	
		
