# link of the task: [https://cs50.harvard.edu/python/2022/psets/3/taqueria/#felipes-taqueria]
menu = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00,
}
total = 0
try:
    while True:
        item = input("Item: ").lower()
        try:
            total += menu[item]
            print(f"Total: ${total:.2f}")
        except:
            pass
except EOFError:
    print(f"Total: ${total:.2f}")
