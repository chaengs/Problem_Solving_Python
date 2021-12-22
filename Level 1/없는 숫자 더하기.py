def solution(numbers):
    answer = 0
    example = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for n in example:
        if n not in numbers:
            answer += n
    return answer