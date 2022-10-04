def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    
    b_idx = 0
    for a in range(0, len(A)) :
        for b in range(b_idx, len(B)):
            if (B[b] > A[a]) :
                b_idx = b + 1
                answer += 1
                break
    
    return answer