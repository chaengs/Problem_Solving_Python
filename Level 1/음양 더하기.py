def solution(absolutes, signs):
    answer = 0
    for i, j in zip(absolutes, signs):
        if j :
            answer += i
        else :
            answer -= i
    return answer

#한 줄로 작성
def solution(absoutes, signs):
    return sum(i if j else -i for i,j in zip(absoutes,signs))