def solution(board, moves):
    # 1. for board 돌리며 moves를 인덱스-1로 돌리기
    # 2. board[moves-1]이 != 0 이면 빈 배열에 담고, 값은 0으로 바꾸기
    # 2-1. 다시 처음부터 탐색 
    # 3. 빈 배열에 넣을 때 앞 값과 같다면 값은 지우고 count += 2
    arr = []
    count = 0
    for loc in moves :
        for search in board :
            doll = search[loc-1]
            if doll != 0 :
                search.pop(loc-1)
                search.insert(loc-1,0)
                # search.replace(doll, 0) -> list형에는 replace가 없음
                if len(arr) != 0 :
                    if arr[-1] == doll :
                        arr.pop()
                        count += 2
                    else : 
                        arr.append(doll)
                else :
                    arr.append(doll)
                break
    return count