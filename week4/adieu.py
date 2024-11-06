import inflect


def main():

    p = inflect.engine()

    names = []

    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        if len(names) == 1:
            print(f"Adieu, adieu, to {names[0]}")
        else:
            print(f"Adieu, adieu, to {p.join(names)}")


if __name__ == "__main__":
    main()
