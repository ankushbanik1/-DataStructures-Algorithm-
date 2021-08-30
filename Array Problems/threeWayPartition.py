def threeWayPartition(self, array, a, b):
	    # code here 
	    lowVal=a
	    highVal=b
	    
    	start = 0
        end = n - 1
        i = 0
     
        # Traverse elements from left
        while i <= end:
     
            # If current element is smaller than
            # range, put it on next available smaller
            # position.
            if array[i] < lowVal:
                array[i],array[start]=array[start],array[i]
                i += 1
                start += 1
     
            # If current element is greater than
            # range, put it on next available greater
            # position.
            elif array[i] > highVal:
                array[i],array[end]=array[end],array[i]
                end -= 1
     
            else:
                i += 1
