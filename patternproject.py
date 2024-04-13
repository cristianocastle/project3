
# defined global variables to avoid error in functions
columns = 'placeholder'
rows = 'placeholder'
height = 'placeholder'
symbol = 'placeholder'


# define function for main menu
def main():

    print()
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
            break
        else:
            print("Enter a valid input: A, B, C, or Q to quit")

    user_choice(choice)
    
# takes user's choice and calls pattern function 
def user_choice(choice):

    if choice == 'A':
        choice_rectangle()
    elif choice == 'B': 
        choice_pyramid()
    elif choice == 'C':
        choice_diamond()
    elif choice == 'Q':
        print('Thank you for your business')
        exit()

# validates user input and returns only postive integers and valid symbol
def validate(userinput):
    
    if userinput == rows:
        value = rows
    elif userinput == columns: 
        value = columns 
    elif userinput == height: 
        value = height
    elif userinput == symbol: 
        value = symbol
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', "N"]
        while value not in symbols:
            value = input("Enter a valid symbol: ")
        return value
    while(True):
        try:
            value = int(value)
            if value <= 0:
                raise Exception
            return value
        except Exception:
            value = input("Enter a valid positive integer: ")


# function to print rectangle shapes 
def rectangle(rows, columns, symbol, pattern):

    #hollow rectangle
    if pattern == 1:
        for x in range(rows):  
            for y in range(columns): 
                if x == 0 or x == rows-1 or y == 0 or y == columns-1:
                    print(symbol + ' ', end='')
                else: 
                    print(' ' + ' ' , end='')
            print()

    #solid rectangle
    elif pattern == 2:
        for x in range(rows):
            for y in range(columns):
                print(symbol + ' ', end=' ')
            print()
    
    #return to main menu after printing shape
    main()


# if user choice is rectangle
def choice_rectangle():
    global rows 
    global columns
    global symbol
    print(' ')
    columns = input('Enter amount of columns: ')
    columns = validate(columns)
    rows = input('Enter amount of rows: ')
    rows = validate(rows)
    symbol = input('Enter symbol: ')
    symbol = validate(symbol)
    print(' ')
    print('1 - Hollow Rectangle')
    print('2 - Solid Rectangle')
    print('0 - Return to main menu')
    print(' ')

    # validate if choice is 0-2
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


# function to print full pyramid shapes
def fullpyramid(height, symbol, pattern2):
   
    # full pyramid 
    if pattern2 == 1:
        if symbol != 'N':
            for i in range(height):
                for j in range(i, height):
                    print(' ' + ' ', end = "")
                for j in range(i):
                    print(symbol + ' ', end = "")
                for j in range(i + 1):
                    print(symbol + ' ', end = "")
                print()
            print()
        else: 
            d = 0
            count = 0
            count1 = 0
            for i in range(1, height + 1):
                for j in range(1, height - i + 1):
                    print('  ', end = "")
                    count += 1
                while d != ((2 * i) - 1):
                    if count <= height -1:
                        print(i + d, end = " ")
                        count += 1
                    else:
                        count1 += 1
                        print(i + d - (2 * count1), end = " ")
                    d += 1
                count1 = count = d = 0
                print()  
            print()

    # inverted full pryamid
    elif pattern2 == 2:
        if symbol != 'N':
            for i in range(height):
                for j in range(i + 1):
                    print(' ', end = "")
                for j in range(i, height - 1):
                    print(symbol, end = "")
                for j in range(i, height):
                    print(symbol, end = "")
                print()
            print()
        else:
            for i in reversed(range(height)):
                print(" " * (height - i - 1), end = "")
                n = (1 + i ** 2) % 10
                for j in range(1 + i * 2):
                    print(n ,end = "")
                    n += 1
                    if n == 10:
                        n = 0
                print()
            print()

    # hollow inverted full pryamid 
    elif pattern2 == 3:
        if symbol != 'N':
            for i in range(height):
                for j in range(i +1):
                    print(' ' + ' ', end = "")
                for k in range(2 * (height -i) - 1):
                    if k == 0 or k == 2 * (height - i - 1) or i == 0:
                        print(symbol + ' ', end = "")
                    else:
                        print(' ' + ' ', end = "")
                print()
            print()
        else: 
            for i in range(1, (height + 1)):
                #print(i)
                if i == 1:
                    pattern = ''
                    for j in range(1, (height + 1)):
                        pattern = pattern + str(j) + " "
                    print(pattern)
                elif i == (height):
                    spaces = " " * (i - 1)
                    print(spaces + '1 ')
                else:
                    spaces = " " * (i - 1)
                    hollowSp = "  " * (height - i - 1)
                    print(spaces + '1 ' + hollowSp + str(height - i + 1) + ' ')
            print()

    #return to main menu after printing shape
    main()


# function to print half pyramid shapes
def halfpyramid(height, symbol, pattern2):

    # half pyramid
    if pattern2 == 1: 
        if symbol != 'N':    
            for i in range(height):
                for j in range(i + 1):
                        print(symbol, end = "")
                print()
        else:
            for i in range(height):
                for j in range(i + 1):
                    print(j + 1, end = "")
                print()

    # inverted half pyramid
    if pattern2 == 2: 
        if symbol != "N":
            for i in range(height):
                for j in range(i, height):
                    print(symbol + ' ', end = "")
                print()
            print()
        else: 
            for i in range(height, 0, -1):
                for j in range(1, i + 1):
                    print(j, end = "")
                print()
        print()

    # hollow inverted half pyramid
    if pattern2 == 3: 
        if symbol != 'N':
            for i in range(height, 0, -1):
                if i == height:
                    print(height * symbol)
                elif 1 < i < height:
                    print(symbol + (i - 2) * ' ' + symbol)
                else:
                    print(symbol)
            print()
        else: 
            for i in range(1, height + 1):
                for j in range(i, height + 1):
                    if i == 1 or j == i or j == height:
                        print(j, end = "")
                    else:
                        print(" ", end = "")
                print()
            print()

    #return to main menu after printing shape
    main()


# if user choice is pyramid 
def choice_pyramid():
    global height
    global symbol
    print(' ')
    height = input('Enter height: ')
    height = validate(height)
    symbol = input('Enter symbol or "N" to use numbers: ')
    symbol = validate(symbol)
    print(' ')
    print('1 - Half Pyramid')
    print('2 - Full Pyramid')
    print('0 - Return to main menu.')
    print(' ')

    # validate if choice is valid
    while (True):
        pattern = int(input('Enter your choice: '))
        if pattern in range(3):
            break
        else:
            print("Enter a valid input 0-2")
        print(' ')

    # if choice is half pyramid call halfpyramid function
    if pattern == 1:
        print('1 - Half Pyramid')  
        print('2 - Inverted Half Pyramid')  
        print('3 - Hollow Inverted Half Pyramid') 
        print('0 - Return to main menu') 
        print(' ')

        while (True):
            pattern2 = int(input('Enter your choice: '))
            if pattern2 in range(4):
                break
            else:
                print("Enter a valid input 0-3")   
            if pattern2 == 0: 
                main()

        halfpyramid(height, symbol, pattern2)
        print(' ')

    # if choice is full pyramid call full pyramid function
    elif pattern == 2: 
        print('1 - Full Pyramid')  
        print('2 - Inverted Full Pyramid')  
        print('3 - Hollow Inverted Full Pyramid') 
        print('0 - Return to main menu') 
        print(' ')

        while (True):
            pattern2 = int(input('Enter your choice: '))
            if pattern2 in range(4):
                break
            else:
                print("Enter a valid input 0-3")   
            if pattern2 == 0: 
                main()

        fullpyramid(height, symbol, pattern2)
        print(' ')

    # if choice is main menu 
    elif pattern == 0:

        print(' ')
        main()
    

# function to print diamond shapes
def diamond(height, symbol, pattern):

    # solid diamond
    if pattern == 1: 
        for i in range(height):
            print(' ' * (height - i - 1) + (symbol + ' ') * (i + 1))
    # Lower half of the diamond
        for i in range(height - 2, -1, -1):
            print(' ' * (height - i - 1) + (symbol + ' ') * (i + 1))

    # hollow diamond
    if pattern == 2: 
        print(' ' * (height - 1) + symbol)  
    # Print upper half of the diamond
        for i in range(1, height):
            print(' ' * (height - i - 1) + symbol + ' ' * (2 * i - 1) + symbol)
        # Print bottom half of the diamond
        for i in range(height - 2, 0, -1):
            print(' ' * (height - i - 1) + symbol + ' ' * (2 * i - 1) + symbol)
        if height > 1:
            print(' ' * (height - 1) + symbol)  # Print bottom of the diamond

    # solid half diamond
    if pattern == 3: 
        for i in range(height):
            print((symbol + ' ') * (i + 1))
        for i in range(height - 2, -1, -1):
            print((symbol + ' ') * (i + 1))

    #return to main menu after printing shape
    main()


# if user choice is diamond 
def choice_diamond():
    
    global height
    global symbol
    print(' ')
    height = input('Enter height: ')
    height = validate(height)
    symbol = input('Enter symbol: ')
    symbol = validate(symbol)
    print(' ')
    print('1 - Solid Diamond')
    print('2 - Hollow Diamond')
    print('3 - Solid Half Diamond')
    print('0 - Return to main menu.')
    print(' ')

    # validate if choice is 0-3
    while (True):
        pattern = int(input('Enter your choice: '))
        if pattern in range(4):
            break
        else:
            print("Enter a valid input 0-2")
        print(' ')

    # call function to print shape 
    diamond(height, symbol, pattern)
    print(' ')

    # if choice is main menu 
    if pattern == 0:
        print(' ')
        main() 


if __name__ == "__main__":
    main()