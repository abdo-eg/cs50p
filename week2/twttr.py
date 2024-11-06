vowels = "AEIOUaeiou"


def remove_vowels():
    string = input("Input: ")
    print("".join(char for char in string if char not in vowels))


remove_vowels()
