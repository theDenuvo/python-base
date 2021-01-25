#Способ 1
s = input()

i = 0
while s[i] == ' ':
    i += 1
s = s[i:]

i = len(s)
while s[i - 1] == ' ':
    i -= 1
s = s[:i]

s_new = s[0]
i = 1
while i < len(s):
    if s[i] != ' ':
        s_new += s[i]
    elif s[i - 1] != ' ':
        s_new += '\n'
    i += 1
print(s_new)


print ('\n' + 'or' + '\n')

#Способ 2
l = s.split()
s1 = '\n'.join(l)
print(s1)