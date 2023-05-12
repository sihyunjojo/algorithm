def solution(n, lost, reserve):
    good_student = [i for i in range(1,n+1) if not i in lost]

    answer = len(good_student)

    for i in reserve:
        if i in lost:
            lost.reomve(i)    

            

    return answer;

n =5
lost = [1,2,3]
reserve = [2,3,4]
answer = 4
print(solution(n,lost,reserve))