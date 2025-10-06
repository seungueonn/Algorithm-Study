def solution(n, results):
    answer = 0
    board = [[0] * (n) for _ in range(n)]
    
    
    for a,b in results:
        board[a-1][b-1] = 1
        board[b-1][a-1] = -1
        
        
    # 정확하게 순위를 매길 수 있는 선수 
    
    # 플로이드 워셜 : 모든 지점에서 다른 모든 지점까지의 최단경로 모두 구하기
    # 플로이드 워셜 알고리즘은 DP 알고리즘에 속한다. 왜냐하면 만약 노드의 개수가 N개라고 할 때, N번 만큼의 단계를 반복하며 '점화식에 맞게' 2차원 리스트를 갱신하기 때문에 DP라고 볼 수 있다. <--> 다익스트라는 그리디 알고리즘에 속한다고 볼 수 있다.
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or board[i][j] in [1,-1]:
                    continue
                if board[i][k] == board[k][j] == 1: # i가 k를 이기고 k가 j를 이기면 i가 j를 이긴다
                    board[i][j] = 1
                    board[j][i] = board[k][i] = board[j][k] = -1
    
    for row in board:
        if row.count(0) == 1:
            answer += 1
    return answer
    
    
    return answer