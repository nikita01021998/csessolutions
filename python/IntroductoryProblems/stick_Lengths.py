n, ans = int(input()), 0
l = list(map(int, input().strip().split()))
l.sort()
prefix, suffix = [0] * n, [0] * n
prefix[0], suffix[n-1] = l[0], l[n-1]
for i in range(1, n) :
	prefix[i] = prefix[i-1] + l[i]
i = n-2
while i >= 0:
	suffix[i] = suffix[i+1] + l[i]
	i = i - 1
ans = min(abs(suffix[1] - l[0] * (n-1)), (n - 1) * l[n-1] - prefix[n-2])
for i in range(1, n-1) :
	a = (i) * l[i] - prefix[i-1]
	b = suffix[i+1]  - (n-1-i) * l[i]
	ans = min(ans, a + b)
print(ans
