Expression = input("Expression: ")

operator = Expression.split()
print("operator is: " + operator[1])
match operator[1]:
    case "+":
        print(float(int(operator[0]) + int(operator[2])))
    case "-":
        print(float(int(operator[0]) - int(operator[2])))
    case "*":
        print(float(int(operator[0]) * int(operator[2])))
    case "/":
        print(float(int(operator[0]) / int(operator[2])))
