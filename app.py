water = {}
gas = {}

def main():
    while True:
        print("Meter Monitor")
        operation = input("Choose operation: add, check, quit: ")
        if operation == "add":
            meter = input("Choose what meter do you want to add (water or gas): ")
            month = input("Enter the month: ")
            value = input("Enter the current value: ")
            addValue(meter, month, value)
        elif operation == "check":
            meter = input("Choose what meter do you want to check (water or gas): ")
            checkValue(meter)
        elif operation == "quit":
            break
        else: print("Enter the correct operation!")

def addValue(meter, month, value):

    if meter == "water":
        water[month] = value

    elif meter == "gas":
        gas[month] = value

    else: raise ValueError

    addValue_test_dict = {'Meter': meter, month: value}
    return addValue_test_dict

def checkValue(meter):
    if meter == "water":
        if water == {}: 
            print("There are no values!")
        else: 
            for (x, y) in water.items():
                print(x + ": " + y)
            return water

    elif meter == "gas":
        if gas == {}:
            print("There are no values!")
        else: 
            for (x, y) in gas.items():
                print(x + ": " + y)
            return gas
    
    else: raise ValueError

if __name__ == '__main__':
    main()

#comment