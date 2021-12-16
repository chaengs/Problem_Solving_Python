def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        new_arr = str(bin(i|j)[2:])
        new_arr = new_arr.zfill(n)
        new_arr = new_arr.replace('1','#')
        new_arr = new_arr.replace('0',' ')
        answer.append(new_arr)
    return answer