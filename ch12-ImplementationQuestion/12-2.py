# 12-2 : 문자열 재정렬

s = input()

result = []
value = 0

for x in s:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))