# 소수인지 확인하는 법 : 2부터 주어진 수의 제곱근 값까지 나눠보기 math.sqrt()
import math
from itertools import combinations

def check(x) :
    new = int(math.sqrt(x))+1
    for j in range(2, new) :
        if x % j == 0 :
            return False
    return True

def solution(nums):
    answer = 0
    com = list(combinations(nums,3))
    for i in range(len(com)):
        new_num = sum(com[i])
        if check(new_num):
            answer += 1
    return answer
