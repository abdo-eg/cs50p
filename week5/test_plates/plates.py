# task link: [https://cs50.harvard.edu/python/2022/psets/2/plates/]
import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    pattern = r"^[A-Za-z]{2,5}[1-9][0-9][0-9]?$|^[A-Za-z]{2,6}$"
    return re.match(pattern, plate) is not None


if __name__ == "__main__":
    main()
