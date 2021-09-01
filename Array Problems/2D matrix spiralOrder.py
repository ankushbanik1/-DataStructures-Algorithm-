class Solution:
	def spiralOrder(self, listi: List[List[int]]) -> List[int]:
		ans = []
		n,m = len(listi),len(listi[0])
		minr,minc = 0,0
		maxr,maxc = n,m
		tot = n * m
		cnt = 0
    
		while(cnt<tot):
			#left
			if cnt < tot:
				for i in range(minc,maxc):
					j = minr
					ans.append(listi[j][i])
					cnt += 1
			minr += 1

			#down
			if cnt < tot:
				for i in range(minr,maxr):
					j = maxc-1
					ans.append(listi[i][j])
					cnt += 1
			maxc -= 1

			#right
			if cnt < tot:
				for i in range(maxc-1,minc-1,-1):
					j = maxr - 1
					#print(i,j)
					ans.append(listi[j][i])
					cnt += 1
			maxr -= 1

			#up
			if cnt < tot:
				for i in range(maxr-1,minr-1,-1):
					j = minc
					ans.append(listi[i][j])
					cnt += 1
			minc += 1
		return ans
