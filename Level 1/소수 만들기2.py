# 소수인지 확인하는 법 : 2부터 주어진 수의 제곱근 값까지 나눠보기 math.sqrt()
from itertools import combinations

def solution(nums):
    answer = 0
    com = combinations(nums,3)
    for i in com:
        new_num = sum(i)
        for j in range(2, int(new_num**0.5)+1):
            if new_num % j == 0:
                break
        else : answer += 1
    return answer