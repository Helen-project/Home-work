def main():
    # First task
    number = input('Please enter an integer number')
    print(f'The result of float number is - {float(number)}')
    # Second task
    number = str(input("Please enter a float number"))
    print(f'You are enter a {type(number)} type')
    # Convert from string to float
    convert_to_float = float(number)
    # Convert from float to integer
    convert_to_int = int(convert_to_float)
    print(f'The result of integer number is - {convert_to_int}')


if __name__ == '__main__':
    main()

