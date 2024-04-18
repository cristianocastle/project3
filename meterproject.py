import random
from art import * 

# account number randomly generated
accnum = random.randint(1000, 9000)
accnum = accnum + 1

# customer code
while (True):
    code = input("Enter customer code: ")
    code = code.upper()
    if code == "R" or code == "C" or code == "I":
        break
    else:
        print("Invalid customer code")

name = input("Enter name: ")
address = input("Enter address: ")

# validate if phone number is 10 digits
phone = input("Enter your phone number: ")
while len(phone) != 10:
    print("enter a valid phone number")
    phone = input("Enter your phone number: ")
else:
    exit

# user inputs meter readings
while (True):
    beginning = int(input("Enter beginning meter reading: "))
    if beginning not in range(0, 999999999):
        print("enter a valid number")
    else:
        break

while (True):
    ending = int(input("Enter ending meter reading: "))
    if ending not in range(0, 999999999):
        print("enter a valid number")
    else:
        break

# if ending is bigger than beginning
if ending >= beginning:
    g = ((ending - beginning) * .1)

# if meter resets
elif beginning > ending:
    g = (((ending - beginning) + 1000000000) * .1)


def cost(code, g):
    # residential code
    if code == "R":
        cost = 5 + (0.0005 * g)
        return cost

        # commercial code
    elif code == "C":
        if g > 4000000:
            cost = 100 + ((g - 4000000) * 0.00025)
        elif g < 4000000:
            cost = 1000
        return cost

        # industrial code
    elif code == "I":
        if g < 4000000:
            cost = 1000
        elif (g > 4000000) and (g < 10000000):
            cost = 200
        elif g > 10000000:
            cost = 2000 + ((g - 10000000) * 0.00025)
        return cost


    else:
        print("Customer code: ", code)
        print("Invalid input (customer code)")


bill = cost(code, g)



if code == "R" or code == "C" or code == "I":
    x = text2art("West   Coast   Water")

    print(x)
    print("Name: ", name)
    print("Address: ", address)
    print("Phone: ", phone)
    print("Account Number:", accnum)
    print(text2art("Invoice"))

    # print customer code
    print(f"customer code = {code}")

    # print meter reading with 9 digits
    print(f"beginning meter reading = {beginning : 09d}")
    print(f"ending meter reading = {ending : 09d}")

    # print gallons of water used including 10th of a gallon
    print(f"gallons of water used = {g:.1f}")

    # print amount of money billed including cents
    print(f"amount of money billed = ${bill:.2f}")

    barcode = decor("barcode1")
    print(" ")
    print(barcode, barcode, barcode)
    print(' ')

while (True):
    answer = input('Would you like to run again? (y/n) ')
    if answer == 'y':
        print(' ')
        while (True):
            code = input("Enter customer code: ")
            code = code.upper()
            if code == "R" or code == "C" or code == "I":
                break
            else:
                print("Invalid customer code")

        name = input("Enter name: ")
        address = input("Enter address: ")

        # validate if phone number is 10 digits
        phone = input("Enter your phone number: ")
        while len(phone) != 10:
            print("enter a valid phone number")
            phone = input("Enter your phone number: ")
        else:
            exit

        # user inputs meter readings
        while (True):
            beginning = int(input("Enter beginning meter reading: "))
            if beginning not in range(0, 999999999):
                print("enter a valid number")
            else:
                break

        while (True):
            ending = int(input("Enter ending meter reading: "))
            if ending not in range(0, 999999999):
                print("enter a valid number")
            else:
                break

        # if ending is bigger than beginning
        if ending >= beginning:
            g = ((ending - beginning) * .1)

        # if meter resets
        elif beginning > ending:
            g = (((ending - beginning) + 1000000000) * .1)

        if code == "R" or code == "C" or code == "I":
            x = text2art("Pacific Water Co.")
            print(x)
            print("Name: ", name)
            print("Address: ", address)
            print("Phone: ", phone)
            print("Account Number:", accnum + 1)
            print(text2art("Invoice"))

            # print customer code
            print(f"customer code = {code}")

            # print meter reading with 9 digits
            print(f"beginning meter reading = {beginning : 09d}")
            print(f"ending meter reading = {ending : 09d}")

            # print gallons of water used including 10th of a gallon
            print(f"gallons of water used = {g:.1f}")

            # print amount of money billed including cents
            print(f"amount of money billed = ${bill:.2f}")

            barcode = decor("barcode1")
            print(" ")
            print(barcode, barcode, barcode)
            print(' ')
    else:
        break