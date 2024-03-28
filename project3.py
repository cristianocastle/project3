

# define function for main menu
def main():
    print('Welcome to the Pattern Print Shop. Please select from the following options:')
    print('A - To print a Rectangle Pattern')
    print('B - To print a Pyramid Pattern')
    print('C - To print a Diamond Pattern')
    print(' ')
    print('Q - Quit.')
    print(' ')

    # return choice of user
    while (True):
        choice = input('Enter your choice: ')
        if choice == 'A' or choice == 'B' or choice == 'C' or choice == 'Q':
            return choice
            break
        else:
            print("Enter a valid input A, B, C, or Q to quit")


# call function to get choice
choice = main()


# terminate program if user quits
if choice == 'Q': 
    exit()

# define function for rectangle shapes 
def rectangle(columns, rows, symbol, pattern):

    #hollow rectangle
    if pattern == 1:
        for x in range(rows):
            for y in range(columns):
                print(symbol, end=' ')
            print()
            return 
        
    #solid rectangle
    elif pattern == 2:
        for x in range(rows):
            for y in range(columns):
                print(symbol, end=' ')
            print()
            return 

# if choice is rectangle
if choice == 'A':
    print(' ')
    columns = int(input('Enter amount of columnsumns: '))
    rows = int(input('Enter amount of rows: '))
    symbol = input('Enter symbol: ')
    print(' ')
    print('1 - Hollow Rectangle')
    print('2 - Solid Rectangle')
    print('3 - Return to main menu')
    print(' ')

    # validate if choice is valid
    while (True):
        pattern = int(input('Enter your choice: '))
        if pattern in range(1, 4):
            break
        else:
            print("Enter a valid input 1-3")

    # call function to print shape of choice or main menu
    if pattern == 1 or pattern == 2:
        finalshape = rectangle(columns, rows, symbol, pattern)
        print(finalshape)
    elif pattern == 3:
        print(' ')
        main()



            
    
