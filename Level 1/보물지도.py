def solution(n, arr1, arr2):
    answer = []
    new_arr1 = []
    new_arr2 = []
    for i in range(n):
        new = str(format(arr1[i],'b'))
        new2 = str(format(arr2[i], 'b'))
        if len(new) != n :
            new = '0'*(n-len(new)) + new
        if len(new2) != n :
            new2 = '0'*(n-len(new2)) + new2
        new_arr1.append(new)
        new_arr2.append(new2)

    for i in range(n):
        key = ''
        for j in range(n):
            if int(new_arr1[i][j]) + int(new_arr2[i][j]) == 0 :
                key += ' '
            else :
                key += '#'
        answer.append(key)
    return answer
