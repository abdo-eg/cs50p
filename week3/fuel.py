def main():
    get_fuel()

def get_fuel():
    while True:
        fuel=input('Fraction: ')
        fuel = fuel.split('/')
        if len(fuel)!= 2 : #here function will accept '/' only
            get_fuel()
        try:

            x,y = int(fuel[0]), int(fuel[1])

            if x > y:
                get_fuel()
            value = round((x/y)*100)
            if value >=99:
                print("F")
            elif value <=1:
                print("E")
            else:
                print(value,"%",sep='')
            break
        except:
            pass
main()


#Link of the task: [https://cs50.harvard.edu/python/2022/psets/3/fuel/]

