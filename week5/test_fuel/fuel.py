def main():
    fraction = input("Fraction: ")
    print(convert(fraction))

def convert(fraction):
    while True:
        # Ensure the input contains a '/'
        if "/" not in fraction:
            fraction = input("Fraction: ")
            continue

        x, y = fraction.split("/")

        try:
            # Attempt to convert the input to integers
            x = int(x)
            y = int(y)

            # Handle invalid fractions where the numerator is larger than the denominator
            if x > y:
                fraction = input("Fraction: ")
                continue

            # Compute the percentage
            percentage = round((x / y) * 100)
            return percentage

        except ValueError:
            # Handle non-integer values by raising the exception
            raise ValueError("Invalid input, please enter a fraction in the format x/y.")

        except ZeroDivisionError:
            # Handle division by zero by raising the exception
            raise ZeroDivisionError("Denominator cannot be zero.")

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
