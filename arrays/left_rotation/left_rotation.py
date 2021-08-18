def solve(a, d):
	return(a[d:]+a[:d])

# Complete the solve function below.
def solve(a, d):
	i = d%len(a)
	return(a[i:]+a[:i])