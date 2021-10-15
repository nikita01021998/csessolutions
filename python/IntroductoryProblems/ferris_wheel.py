n, x = list(map(int, input().strip().split()))
l = list(map(int, input().strip().split()))
i, j, count = 0, n-1, 0
l.sort()
while i<=j :
	sum, c = l[j], 0
	while i <= j and sum + l[i] <=x and c < 1:
		sum = sum + l[i]
		i+=1
		c+=1
	j=j-1
	count+=1
print(count)
