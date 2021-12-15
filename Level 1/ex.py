# string = '~!@#$%^&*()=+[{]}:?,<>/'
# str = '3'
# length = len(str)
# str2 = str.replace('3','')
# print(str2)

# for i in range(len(string)) :
#     j = string[i]
#     # print(str.find(j))
#     if str.find(j) != -1:
#         str = str.strip(j)
#         print(str)

str = "...!@BaT#*..y.abcdefghijklm"

if '..' in str:
    while '..' in str :
        str = str.replace('..','.')
        print(str)