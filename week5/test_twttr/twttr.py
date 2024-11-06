# task link [https://cs50.harvard.edu/python/2022/psets/2/twttr/]
def main():
    string = input("Input: ")

    print(shorten(string))


def shorten(string):
    vowels = "AEIOUaeiou"
    return "".join(char for char in string if char not in vowels)


if __name__ == "__main__":
    main()

