# from collections import deque
# def right(idx, d): 
#     if idx > 3:
#         return
#     # 같은 극이 아니면 회전
#     if sawtooth[idx - 1][2] != sawtooth[idx][6]:
#         right(idx + 1, -d)
#         sawtooth[idx].rotate(d)


# def left(idx, d):
#     if idx < 0:
#         return
#     # 같은 극이 아니면 회전
#     if sawtooth[idx][2] != sawtooth[idx + 1][6]:
#         left(idx - 1, -d)
#         sawtooth[idx].rotate(d)


# sawtooth = [deque(list(map(int, input()))) for _ in range(4)]
# k = int(input())   # 회전 횟수

# for _ in range(k):
#     idx, d = map(int, input().split())
#     idx -= 1
#     left(idx - 1, -d)
#     right(idx + 1, -d)

#     sawtooth[idx].rotate(d)


# score = 0
# for i in range(4):
#     if sawtooth[i][0] == 1:
#         score += 2 ** i

# print(score)


# 점수
from collections import deque

n= 4
def score():
    score = 0
    for i in range(4):
        if arr[i][0] == 1:
            score += 2 ** i

    return score

def right(idx,d):
    if idx > 3:
        return
    
    if arr[idx-1][2] != arr[idx][6]:
        right(idx+1,-d)
        arr[idx].rotate(d) # 오른쪽으로 배열 한칸씩 이동 

def left(idx,d):
    if idx < 0:
        return
    
    if  arr[idx][2] != arr[idx+1][6]:
        left(idx-1,-d)
        arr[idx].rotate(d)


arr=[]
for _ in range(4):
    arr.append(deque(list(map(int,input().strip()))))
    # 12시방향부터 시계방향 순서대로 / n극은 0 s극은 1

k=int(input().strip())
for _ in range(k): # 회전 횟수
    index,direction=map(int,input().split()) # 회전시킨 톱니바퀴 번호, 방향(1시계 / -1반시계)

    index -= 1 # index니까 

    left(index-1, -direction)
    right(index+1, -direction)

    arr[index].rotate(direction)


print(score())