def solution(new_id):
    newId = new_id
    string = '~!@#$%^&*()=+[{]}:?,<>/'
    while True:
        newId = newId.lower()
        for i in range(len(string)) :
            j = string[i]
            if newId.find(j) != -1:
                newId = newId.replace(j,'')
        while '..' in newId :
            newId = newId.replace('..','.')
        
        if newId[0] == '.':
            newId = newId[1:] if len(newId) > 1 else '.'
        
        if newId[-1] == '.':
            newId = newId[:-1]
        # if len(newId) > 0 :
        #     if newId[0] == '.' :
        #         newId = newId.replace(newId[0],'')
        #         if len(newId) == 0 :
        #             newId = newId + 'a'
        #     if newId[-1] == '.' :
        #         newId = newId.replace(newId[-1],'')
        #         if len(newId) == 0 :
                    # newId = newId + 'a'
        if len(newId) == 0 :
            newId = 'a'
        if len(newId) > 15 :
            newId = newId[:15]
            if newId[-1] == '.' :
                newId = newId[:-1]
        
        if len(newId) <= 2 :
            while len(newId) < 3 :
                newId = newId + newId[-1]
        answer = newId
        break
    return answer
#2번 조건(특수문자 지우는 것)은 이런 코드로도 가능하다
for c in new_id:
    if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
        answer += c