n1 = int(input())
n2 = int(input())

total_sum1 = 0
expression_str1 = ""

for i in range(1, n1):
    term_value = i * (i + 1)
    total_sum1 = total_sum1 + term_value
    
    term_str = str(i) + "*" + str(i + 1)
    
    if i == 1:
        expression_str1 = term_str
    else:
        expression_str1 = expression_str1 + "+" + term_str

print(expression_str1 + "=" + str(total_sum1))


total_sum2 = 0
expression_str2 = ""

for i in range(1, n2):
    term_value = i * (i + 1)
    total_sum2 = total_sum2 + term_value
    
    term_str = str(i) + "*" + str(i + 1)
    
    if i == 1:
        expression_str2 = term_str
    else:
        expression_str2 = expression_str2 + "+" + term_str

print(expression_str2 + "=" + str(total_sum2))