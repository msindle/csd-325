def main():
    intro()
    try:
        gallons_needed = float(input('Enter the number of gallons:'))
        gallons_to_liters(gallons_needed)
    except:
        print('An exception has occurred, try again by entering only a number:')
        print()
        main()

def intro():
    print('''This program converts measurements')
    from gallons to liters. For your
    reference the formula is:
    1 gallon = 3.785 fluid ounces''')
    print()

def gallons_to_liters(gallons):
    liters = gallons * 3.785
    print('That converts to', liters, 'liters.')

main()