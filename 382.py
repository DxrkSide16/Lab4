a = int(input())
b = int(input())
c = int(input())
d = int(input())

# 1. Друк верхнього рядка (заголовка)
print("\t", end="") 
for j in range(c, d + 1):
    print(j, end="")
    if j < d:
        print("\t", end="")
print() 

# 2. Друк рядків з даними
for i in range(a, b + 1):
    print(i, end="\t") 
    for j in range(c, d + 1):
        product = i * j
        print(product, end="")
        if j < d:
            print("\t", end="")
    print()