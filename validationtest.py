

# this function should only return positive integers and valid symbols
def validate_input(input):

    if input == rows:
        value = rows
    elif input == columns: 
        value = columns 
    elif input == height: 
        value = height
    elif input == symbol: 
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', "N"]
        while symbol not in symbols:
            symbol = input("Enter a valid symbol: ")
        return symbol
    while(True):
        try:
            value = int(value)
            if value <= 0:
                raise Exception
            return value
        except Exception:
            value = input("Enter a valid positive integer: ")



# test to see if validation function works 
def test():
    global rows 
    global columns
    global height
    global symbol

    rows = int(input('enter input '))
    rows = validate_input(rows)
    print(rows)

    columns = int(input('enter input '))
    columns = validate_input(columns)
    print(columns)

    height = int(input('enter input '))
    height = validate_input(height)
    print(height)
    
    symbol = '$'
    validate_input(symbol)
    print(symbol)

test()