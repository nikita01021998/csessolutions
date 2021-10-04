val = int(input())
l = [[None] * 2] * val
for i in range(0, val) :
	l[i] = list(map(int, input().split()))
l.sort()
p = l[0]
count = 0
for i in range(1, val) :
	if (l[i][0] < p[1] or p[1] > l[i][1]) == False :
		count+=1
		p = l[i]
	elif p[1] > l[i][1]:
		p = l[i]
print(count+1)	