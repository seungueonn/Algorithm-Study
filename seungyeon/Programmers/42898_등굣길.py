def solution(m, n, puddles):
    answer = 0
    
    dp=[[0] * (m+1) for _ in range(n+1)]
    
    new_puddles=[]
    
    for a,b in puddles:
        new_puddles.append((b,a))
    
    
    dp[1][1] = 1
    
    for i in range(n+1):
        for j in range(m+1):
            
            if i == 1 and j == 1:
                continue
            if (i,j) in new_puddles:
                dp[i][j] = 0
            else :
                dp[i][j] = (dp[i][j-1] + dp[i-1][j])%1000000007
    
    
    return dp[n][m]