import sys
import os


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
            # print(f"The file {sys.argv[1]} exists.")
            if sys.argv[1].endswith(".py"):
                print(get_loc())
            else:
                sys.exit("Not a Python file")
        else:
            print(f"The file {sys.argv[1]} does not exist.")


def get_loc():
    with open(sys.argv[1], "r") as file:
        lines = 0
        for i in file:
            i = i.strip()
            # skip lines
            if i == "" or i.startswith("#"):
                pass
            else:
                lines += 1
        return lines


if __name__ == "__main__":
    main()

