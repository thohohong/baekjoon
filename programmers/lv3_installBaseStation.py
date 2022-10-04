def solution(n, stations, w):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    idx = w + 1
    s = 0
    while(True) :
        if (idx > n + w) :
            break;
        if (s >= len(stations)) :
            answer += 1
            idx += 2 * w + 1
        elif (idx - w < stations[s] - w) :
            answer += 1
            idx += 2 * w + 1
        else :
            idx = stations[s] + 2 * w + 1
            s += 1

    return answer