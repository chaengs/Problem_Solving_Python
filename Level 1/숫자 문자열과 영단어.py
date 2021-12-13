# 1
def solution(s):
    number = {
        'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9
    }
    
    new = s
    for key, value in number.items() :
        new = new.replace(key, str(value))
    return int(new)

# 2
def solution(s):
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(eng)):
        s = s.replace(eng[i], str(i))

    return int(s)