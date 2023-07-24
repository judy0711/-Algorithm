N = int(input())

for _ in range(N):
	rep, word = input().split()
	for j in word:
		print(j * int(rep), end = '')
	print()