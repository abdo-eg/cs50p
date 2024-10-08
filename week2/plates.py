import re
plate = input("Plate: ")

def main():
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    pattern = r'^[A-Za-z]{2,5}[1-9][0-9]?$|^[A-Za-z]{2,6}$'
    return re.match(pattern, plate) is not None
main()
