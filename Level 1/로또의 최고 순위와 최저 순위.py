def solution(lottos, win_nums):
    # lottos =  list(map(int, input().split()))
    # win_nums = list(map(int, input().split()))
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero = lottos.count(0)
    count = 0
    for i in lottos:
        if i in win_nums:
                count += 1
    higher = rank[zero+count]
    lower = rank[count]
    return [higher, lower]

# 1. 0의 개수 구하기
# 2. count = lottos와 win_nums가 몇개 일치하는지 개수 확인
# 3. 가장 높은 등수 : count 개수 + 0의 개수
# 4. 가장 낮은 등수 : count 개수

