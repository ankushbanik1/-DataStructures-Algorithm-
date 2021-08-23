class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Alternetive -------->>
        #only run this single line
        # return [math.comb(rowIndex,i) for i in range(rowIndex+1)]
        # ------------------------------------------------------------------------
        arr=[]
        for i in range(0,rowIndex+1):
            temp=[]
            if i==0:
                temp.append(1)
                arr.append(temp)
            elif i==1:
                temp.append(1)
                temp.append(1)
                arr.append(temp)
            else:
                for j in range(0,i+1):
                    if j==0 or j==i:
                        temp.append(1)
                    else:
                        temp.append(arr[i-1][j-1]+arr[i-1][j])
                arr.append(temp)
        return arr[rowIndex]
                    
