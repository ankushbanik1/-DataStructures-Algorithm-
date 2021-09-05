# Python3 program to check if string
# str1 is subof str2 or not.

# Function two check A
# is shuffled subof B
# or not
def isShuffledSubstring(A, B):
	n = len(A)
	m = len(B)

	# Return false if length of
	# A is greater than
	# length of B
	if (n > m):
		return False
	else:

		# Sort A
		A = sorted(A)

		# Traverse B
		for i in range(m):

			# Return false if (i+n-1 >= m)
			# doesn't satisfy
			if (i + n - 1 >= m):
				return False

			# Initialise the new string
			Str = ""

			# Copy the characters of
			# B in str till
			# length n
			for j in range(n):
				Str += (B[i + j])

			# Sort the str
			Str = sorted(Str)

			# Return true if sorted
			# of "str" & sorted
			# of "A" are equal
			if (Str == A):
				return True

# Driver Code
if __name__ == '__main__':
	
	# Input str1 and str2
	Str1 = "geekforgeeks"
	Str2 = "ekegorfkeegsgeek"

	# Function return true if
	# str1 is shuffled substring
	# of str2
	a = isShuffledSubstring(Str1, Str2)

	# If str1 is subof str2
	# print "YES" else print "NO"
	if (a):
		print("YES")
	else:
		print("NO")

# This code is contributed by mohit kumar 29
