path = input()

current_part = ""

for char in path:
    if char == '\\':
        print(current_part)
        current_part = ""
    else:
        current_part = current_part + char

print(current_part)