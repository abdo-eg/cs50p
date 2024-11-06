# link of the task : [https://cs50.harvard.edu/python/2022/psets/3/grocery/]
orders = {}

try:
    while True:
        order = input("").upper()
        if order in orders:
            orders[order] += 1
        else:
            orders[order] = 1
except EOFError:
    orders = dict(sorted(orders.items()))
    for order in orders:
        print(orders[order], order)
