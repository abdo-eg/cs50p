snake_case = ""
camelCase = input("name: ")
for c in camelCase:
    if c.islower():
        snake_case += c
    else:
        snake_case += "_" + c.lower()
print(snake_case)
