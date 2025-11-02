number_str = input("Number: ")
digit_to_remove = input("Number to remove: ")

result_str = ""

for char in number_str:
    if char != digit_to_remove:
        result_str += char

print(result_str)  