s1 = input()
s2 = input()

s1_clean = ""
for char in s1:
    if char != ' ':
        s1_clean = s1_clean + char

s2_clean = ""
for char in s2:
    if char != ' ':
        s2_clean = s2_clean + char

s1 = s1_clean
s2 = s2_clean

total1 = int(s1[0])
current_op = ''
for char in s1[1:]:
    if char == '+':
        current_op = '+'
    elif char == '-':
        current_op = '-'
    else:
        num = int(char)
        if current_op == '+':
            total1 = total1 + num
        elif current_op == '-':
            total1 = total1 - num

print(total1)

total2 = int(s2[0])
current_op = ''
for char in s2[1:]:
    if char == '+':
        current_op = '+'
    elif char == '-':
        current_op = '-'
    else:
        num = int(char)
        if current_op == '+':
            total2 = total2 + num
        elif current_op == '-':
            total2 = total2 - num

print(total2)