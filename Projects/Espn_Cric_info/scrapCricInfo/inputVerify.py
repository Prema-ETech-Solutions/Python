

def wholeNumber(msg):
    while True: 
        try:
            x = int(input(msg))
            break
        except ValueError:
            print('Please only input digits')
    
    return x

def decimalNumber(msg):
    while True: 
        try:
            x = float(input(msg))
            break
        except ValueError:
            print('Please only input digits')
    
    return x