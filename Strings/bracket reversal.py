# Python3 program to find minimum number of
# reversals required to balance an expression

# Returns count of minimum reversals for
# making expr balanced. Returns -1 if
# expr cannot be balanced.
def countMinReversals(expr):

	length = len(expr)

	# length of expression must be even to
	# make it balanced by using reversals.
	if length % 2:
		return -1

	# To store number of reversals required.
	ans = 0

	# To store number of unbalanced
	# opening brackets.
	open = 0

	# To store number of unbalanced
	# closing brackets.
	close = 0

	for i in range(0, length):

		# If current bracket is open
		# then increment open count.
		if expr[i] == "":
			open += 1

		# If current bracket is close, check if it
		# balances opening bracket. If yes then
		# decrement count of unbalanced opening
		# bracket else increment count of
		# closing bracket.
		else:
			if not open:
				close += 1
			else:
				open -= 1
		
	ans = (close // 2) + (open // 2)

	# For the case: "" or when one closing
	# and one opening bracket remains for
	# pairing, then both need to be reversed.
	close %= 2
	open %= 2
	
	if close > 0:
		ans += 2

	return ans

# Driver Code
if __name__ == "__main__":

	expr = "}}{{"
	print(countMinReversals(expr))

# This code is contributed by Rituraj Jain
