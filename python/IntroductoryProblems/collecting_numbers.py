val = int(input())
l = list(map(int, input().split()))
mymap = {}
for i in range(0, len(l)):
	mymap[l[i]] = i	
l.sort()
currIndex, ans = len(l) + 1, 0
for i in range(0, len(l)):
    ind = mymap[l[i]]
    if currIndex > ind :
       ans += 1
    currIndex = ind
print(ans)      	