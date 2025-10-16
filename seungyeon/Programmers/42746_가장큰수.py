def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))   
    numbers.sort(key = lambda x : x*3, reverse=True) # 93,3,30 있을 때 93,30,3 순으로 정렬되어야함, numbers 원소의 최대값 1000이기때문에 3자리까지 고려해서 {939|393,333|333,303|030} 해서 정렬해야한다.
    
    for n in numbers:
        answer += n
    return str(int(answer))