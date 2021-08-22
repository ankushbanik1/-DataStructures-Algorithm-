
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        
        intervals=sorted(intervals)
        output=intervals[0]

        res=[]

        for i in range(1,len(intervals)):
            if intervals[i][0]<output[1]:
                output[1]=max(output[1],intervals[i][1])

            else:
                res.append(output.copy())

                output[0]=intervals[i][0]
                output[1]=intervals[i][1]


        res.append(output)
        return res
                   
