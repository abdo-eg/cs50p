import random
def main():
    level = get_level()
    score =0
    # loop
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        attempts = 0
        while attempts <3:
            try:
                guess = int(input(f" {x} + {y} = "))
                if guess == correct_answer:
                    score +=1
                    break
                else:
                    print("EEE")
                    attempts +=1
            except ValueError:
                print("EEE")
                attempts +=1
        if attempts == 3 :
            print(f" {x} + {y} = {correct_answer}")
    print(f"Score: {score}")
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except:
            pass
def generate_integer(level):
    if level ==1:
        return random.randint(0, 9)
    elif level==2:
        return random.randint(10, 99)
    elif level ==3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid Level")
if __name__ == "__main__":
    main()

