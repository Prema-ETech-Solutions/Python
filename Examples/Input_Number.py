valid = False

while not valid: 
    try:
        x = int(input('Enter an integer: '))
        valid = True 
    except ValueError:
        print('Please only input digits')

input()