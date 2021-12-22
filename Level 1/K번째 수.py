def solution(array, commands):
    answer = []
    for c in commands :
        i = c[0]-1
        j = c[1]
        k = c[2]-1
        new_arr = sorted(array[i:j])
        result = new_arr[k]
        answer.append(result)
    return answer