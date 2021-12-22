def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    #1,4,7은 L
    #3,6,9는 R
    #2,5,8,0은 각자 위치의 숫자의 차 절대값 구하기 -> 3으로 나눈 몫과 나머지로 이동 횟수를 구할 수 있음
    #왼손, 오른손 배열을 만들어 위치 표시하기
    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7 :
            answer += 'L'
            left = numbers[i]
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9 :
            answer += 'R'
            right = numbers[i]
        else :
            numbers[i] = 11 if numbers[i] == 0 else numbers[i]
            left_loc = abs(left - numbers[i])
            right_loc = abs(right - numbers[i])
            left_move = sum(divmod(left_loc, 3))
            right_move = sum(divmod(right_loc, 3))
            if left_move > right_move :
                answer += 'R'
                right = numbers[i]
            elif left_move < right_move :
                answer += 'L'
                left = numbers[i]
            else :
                if hand == 'right' :
                    answer += 'R'
                    right = numbers[i]
                else :
                    answer += 'L'
                    left = numbers[i]
    return answer