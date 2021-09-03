def kthSmallest(mat, n, k): 
    # Your code goes here
    
    sett=[]
    #n=len(matrix)
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            sett.append(mat[i][j])
            
            
    sett=sorted(sett)
    
    return sett[k-1]
        
