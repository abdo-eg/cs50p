from tabulate import tabulate
import sys
import os
import csv


def main():
    get_file()


count_args = len(sys.argv)


def get_file():
    # check args
    if count_args < 2:
        sys.exit("Too few command-line arguments")
    elif count_args > 2:
        sys.exit("Too many command-line arguments")
    else:
        # check file
        if os.path.exists(sys.argv[1]):
            if sys.argv[1].endswith(".csv"):
                print(get_formatted())
            else:
                sys.exit("Not a CSV file")
        else:
            sys.exit("File does not exist")


def get_formatted():
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        # header = next(reader) #next(reader) is used to fetch the first row of the CSV file as the header.
        header = reader.fieldnames
        data = [row for row in reader]
        # Convert the list of dictionaries into a list of rows for tabulate
        rows = [list(row.values()) for row in data]
        return tabulate(rows, headers=header, tablefmt="grid")


if __name__ == "__main__":
    main()

