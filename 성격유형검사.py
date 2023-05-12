def solution(survey, choices):
    result = {'RT':0, 'CF':0, 'JM':0, 'AN':0}
    answer = ''

    for i in survey:
        score = choices.pop(0) -4
        print('score = ' ,score)
        if not i in result:
            i = i[-1::-1]
            result[i] -= score     
        else:
            result[i] += score
        print('어떤걸로 들어갓냐 = ', i)
        print('처음 값 = ',score)       
        print('더해진 값 = ',result[i])
            

    print('result = ' ,result)
    for i in result:
        if result[i] <= 0:
            answer += i[0]
        else:
            answer += i[1]
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))
