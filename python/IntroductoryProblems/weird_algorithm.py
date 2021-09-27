val = int(input())
l = [val]
while val != 1:
	if (val % 2 == 1) :
		l.append(val*3 + 1)
		val = val * 3 + 1
	else :
		l.append(int(val/2))
		val = int(val / 2)

print(*l)