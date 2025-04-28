import sys
input=sys.stdin.readline

n=int(input().rstrip())
arr=[]
plus=[]
minus=[]
answer = 0
for i in range(n):
    
    a = int(input())

    if a > 1:
        plus.append(a)
    elif a <= 0:
        minus.append(a)
    else:
        answer += a

plus.sort(reverse=True)
minus.sort()

for i in range(0,len(plus),2):
    if i+1 >= len(plus):
        answer += plus[i]
    else:
        answer += (plus[i] * plus[i+1])

for i in range(0,len(minus),2):
    if i+1 >= len(minus):
        answer += minus[i]
    else:
        answer += (minus[i] * minus[i+1])

print(answer)
