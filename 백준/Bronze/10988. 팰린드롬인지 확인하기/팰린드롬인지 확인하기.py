word = list(str(input()))
j = len(word) 
result = True
for i in range(j//2):
	if word[i] != word[j - i - 1]:
		result = False
		break
if result:
	print(1)
else:
	print(0)
