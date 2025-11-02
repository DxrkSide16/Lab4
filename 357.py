s1 = input("Введіть слово: ")
s2 = input("Введіть слово: ")

result1 = ""
for i in range(len(s1)):
    if i % 2 == 0:
        result1 = result1 + s1[i]

result2 = ""
for i in range(len(s2)):
    if i % 2 == 0:
        result2 = result2 + s2[i]

print(result1)
print(result2)