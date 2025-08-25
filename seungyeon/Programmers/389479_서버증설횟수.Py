def solution(players,m,k):
    
    server = [0] * len(players) 

    server_cnt = 0
    
    for i in range(len(players)):
        n = 0
        if players[i] >= m:
            n = players[i] // m # 필요한 서버 
            
            add_server_cnt = 1
            if server[i] < n:
                add_server_cnt = n - server[i]
                
                if n * m <= players[i] < (n+1) * m:
                    server_cnt += add_server_cnt
                    
                    for j in range(k):
                        if i+j<len(server):
                            server[i+j] += add_server_cnt
                            
                        else:
                            break
                            
    return server_cnt