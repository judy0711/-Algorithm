def factorial(m):
	num = 1
	for i in range(1, m+1):
		num*= i
	return num

loop = int(input())
for i in range(loop):
	left, right = map(int, input().split())
	bridge = factorial(right) // (factorial(left) * factorial(right-left))
	print(bridge)