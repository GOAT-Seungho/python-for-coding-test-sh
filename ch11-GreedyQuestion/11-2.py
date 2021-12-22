# 11-2 : 곱하기 혹은 더하기

s = input()

if s[0] == '0':
    result = 1
else:
    result = 0

for i in range(len(s)):
    if s[i] == '1' or s[i] == '0':
        result += int(s[i])
    else:
        result *= int(s[i])

print(result)