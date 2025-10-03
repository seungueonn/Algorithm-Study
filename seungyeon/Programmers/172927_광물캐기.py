def solution(picks, minerals):
    answer = 0
    sum = 0
    
    # 하나 선택해서 5개 연속으로 캐고 다음 곡괭이 선택해서 5개 연속 캔다
    # 사용할 곡괭이가 없거나 광산에 있는 모든 광물을 캘 때까지 
    # 최소한의 피로도 
    
    
    # 곡괭이 수
    for i in picks:
        sum += i
        
    num = sum * 5
    
    if len(minerals) > sum:
        minerals = minerals[:num]
        
    new_minerals = [[0,0,0] for _ in range((len(minerals) // 5 + 1))]
    
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            new_minerals[i//5][0] += 1
        elif minerals[i] == 'iron':
            new_minerals[i//5][1] += 1
        elif minerals[i] == 'stone':
            new_minerals[i//5][2] += 1
            
    new_minerals.sort(key=lambda x : (-x[0],-x[1],-x[2]))
    
    for i in new_minerals:
        dia,iron,stone = i
        
        for j in range(len(picks)):
            if picks[j] > 0 and j == 0:
                picks[j] -= 1
                answer += dia+iron+stone
                break
            elif picks[j] > 0 and j == 1:
                picks[j] -= 1
                answer += (5*dia) + iron + stone
                break
            elif picks[j] > 0 and j == 2:
                picks[j] -= 1
                answer += (25*dia) + (5*iron) + stone
                break
                
    
    return answer