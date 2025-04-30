# 왼쪽 위부터 스티커 
# 스티커 오른쪽으로 90도 

Y,X,K=map(int,input().split())

stickers=[]
notebook=[[0] * X for _ in range(Y)]
arr=[ [0] * X for _ in range(Y)]

def rotate(arr):
    y,x=len(arr),len(arr[0])
    rotated_arr=[[0] * y for _ in range(x)]

    for i in range(y):
        for j in range(x):
            rotated_arr[j][y-1-i] = arr[i][j]

    return rotated_arr

def check(x,y,sticker):
    r,c=len(sticker),len(sticker[0])
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1 and notebook[y+i][x+j] == 1:
                return False
    return True


def attach(x,y,sticker):
    r,c=len(sticker),len(sticker[0])

    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                notebook[y+i][x+j] = 1


for i in range(K):
    y,x=map(int,input().split())
    s=[]
    for i in range(y):
        s.append(list(map(int,input().split())))
    stickers.append(s)


for i in range(K):
    curr_sticker = stickers[i]
    rotate_cnt = 0

    while rotate_cnt < 4:
        s_Y, s_X = len(curr_sticker), len(curr_sticker[0])  # y, x 순서 주의
        is_attached = False

        # notebook 범위 내인지 검사하고 붙이기 시도
        if s_Y <= Y and s_X <= X:
            for y in range(Y - s_Y + 1):
                for x in range(X - s_X + 1):
                    if check(x, y, curr_sticker):
                        attach(x, y, curr_sticker)
                        is_attached = True
                        break
                if is_attached:
                    break

        if is_attached:
            break
        else:
            curr_sticker = rotate(curr_sticker)
            rotate_cnt += 1

answer=0
for i in range(Y):
        answer += notebook[i].count(1)

print(answer)