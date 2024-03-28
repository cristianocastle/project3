

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
def rectangle(rows, columns, symbol, pattern):

    #hollow rectangle
    if pattern == 1:
        for x in range(rows):  
            for y in range(columns): 
                if x == 0 or x == rows-1 or y == 0 or y == col-1:
                    print(symbol + " ", end='')
                else: 
                    print(' ' + ' ', end='')
            print()

        
    #solid rectangle
    elif pattern == 2:
        for x in range(rows):
            for y in range(columns):
                print(symbol + ' ', end=' ')
            print()



# if choice is rectangle
if choice == 'A':
    print(' ')
    columns = int(input('Enter amount of columns: '))
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
        if pattern in range(3):
            break
        else:
            print("Enter a valid input 0-2")

    # call function to print shape of choice or main menu
    if pattern == 1 or pattern == 2:
        rectangle(columns, rows, symbol, pattern)
    elif pattern == 0:
        print(' ')
        main()



def pyramid(columns, rows, symbol, pattern2):
   
    # full pyramid 
    if pattern2 == 1:
        break



    # inverted full pryamid
    elif pattern2 == 2:
        break

    # hollow inverted full pryamid 
    elif pattern2 == 3:
        break



def halfpyramid(columns, rows, symbol, pattern2):

    # half pyramid
    if pattern2 == 1:
        break

    # inverted half pyramid 
    elif pattern2 == 2:
        break

    # hollow inverted hollow pyramid
    elif pattern2 == 3:
        break



# if choice is pyramid
if choice == 'B':
    print(' ')
    columns = int(input('Enter amount of columns: '))
    rows = int(input('Enter amount of rows: '))
    symbol = input('Enter symbol: ')
    print(' ')
    print('1 - Half Pyramid')
    print('2 - Full Pyramid')
    print('0 - Return to main menu.')

    # validate if choice is valid
    while (True):
        pattern = int(input('Enter your choice: '))
        if pattern in range(3):
            break
        else:
            print("Enter a valid input 0-2")

    # if choice is half pyramid call halfpyramid function
    if pattern == 1:
        print('1 - Half Pyramid')  
        print('2 - Inverted Half Pyramid')  
        print('3 - Hollow Inverted Half Pyramid') 
        print('0 - Return to main menu') 

        while (True):
            pattern2 = int(input('Enter your choice: '))
            if pattern2 in range(3):
                break
            else:
                print("Enter a valid input 0-3")   
        
        halfpyramid(columns, rows, symbol, pattern)

    # if choice is full pyramid call full pyramid function
    elif pattern == 2: 
        print('1 - Full Pyramid')  
        print('2 - Inverted Full Pyramid')  
        print('3 - Hollow Inverted Full Pyramid') 
        print('0 - Return to main menu') 

        while (True):
            pattern2 = int(input('Enter your choice: '))
            if pattern2 in range(3):
                break
            else:
                print("Enter a valid input 0-3")   
        
        pyramid(columns, rows, symbol, pattern2)

    # if choice is main menu 
    elif pattern == 0:
        print(' ')
        main()
