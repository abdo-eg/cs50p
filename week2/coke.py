price =50

while price > 0:
    print('Amount Due:', price)
    payment = int(input('Insert Coin: '))
    if payment in [5,10,25]:
        price -= payment
print(f'Change Owed: {abs(price)}')
