 n = len(arr)
 # If length of array is even
        if n % 2 == 0:
            z = n // 2
            e = arr[z]
            q = arr[z - 1]
            ans = (e + q) / 2.0
            return ans

        # If length of array is odd
        else:
            z = n // 2
            ans = arr[z]
            return ans
 
