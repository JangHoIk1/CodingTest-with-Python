temp1 = 0
temp2 = 0

arr = [int(input()) for _ in range(9)]

for i in range(9):
	for j in range(i + 1, 9):
		if sum(arr) - (arr[i] + arr[j]) == 100:
			temp1 = arr[i]
			temp2 = arr[j]

arr.remove(temp1)
arr.remove(temp2)
arr.sort()

for i in arr:
	print(i)