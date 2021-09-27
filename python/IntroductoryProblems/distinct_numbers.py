# python3 soln.py < inp.txt
# docker run -it -v /Users/nikita.kumari/Documents/PTE:/code py sh
val = int(input())
l = list(map(int, input().split()))
s = set(l)
print(len(s))