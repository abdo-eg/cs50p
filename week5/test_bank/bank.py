# details about task here--> [https://cs50.harvard.edu/python/2022/psets/1/bank/]
def main():
    greeting = input("Greeting: ")
    print("$", value(greeting), sep="")


def value(greeting):
    greeting = greeting.lower().replace(" ", "")
    if "hello" in greeting:
        return 0
    try:
        if greeting[0] == "h":
            return 20
    except:
        pass
    else:
        return 100


if __name__ == "__main__":
    main()

