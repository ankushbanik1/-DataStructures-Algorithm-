class Solution(object):
    
    def romanToInt(self, s):
        
        
        b=[]

        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in s:

            b.append(roman.get(i))
        for i in range(len(b)-1):
            if abs(b[i])<abs(b[i+1]):
                b[i]=-b[i]

        return sum(b)
