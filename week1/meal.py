def main():
    
    time = input('What time is it? ')
    organized_time = convert(time)

    # set cases
    if 7 <= organized_time <= 8:
        print('breakfast time')
    elif 12 <= organized_time <= 13:
        print('lunch time')
    elif 18 <= organized_time <= 19:
        print('dinner time')

def convert(time):
    hours,minutes = map(int, time.split(':'))
    total_time = ((hours*60) + minutes) / 60
    return total_time

if __name__ == "__main__":
    main()

