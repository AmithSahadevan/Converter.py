# jlt = just like that!
def jlt():

    again = input("\nDo you want to continue?(y/n)/(yes/no): ").lower()

    while again == "yes" or "y":
        if again == "yes" or again == "y":
            try:
                print("\nUsable units: kg, g, lbs, km, mm, m, cm, mi(mile), k(kelvin), f(fahrenheit), c(celsius), d(dollar), r(rupee)")
                print("\nEnter the value that you want to convert (number..)👇")
                inp = float(input(">>> "))
                unit = input("Enter the unit: ").lower()
                con = input("Convert to: ").lower()

                # Temperature

                if unit == "c":
                    if con == "k":
                        converted = inp + 273.15
                        print(f"Converted value is {converted}")
                    elif con == "f":
                        converted = (inp * 1.8)+32
                        print(f"Converted value is {converted}")
                    else:
                        print("cannot convert, try again!(Check the units!)")
                        jlt()
                elif unit == "k":
                    if con == "c":
                        converted = inp - 273.15
                        print(f"Converted value  is {converted}")
                    elif con == "f":
                        converted = (inp - 273.15)*1.8+32
                        print(f"Converted value is {converted}")
                    else:
                        print("cannot convert, try again!(Check the units!)")
                        jlt()
                elif unit == "f":
                    if con == "c":
                        converted = (inp - 32)*0.5556
                        print(f"Converted value is {converted}")
                    elif con == "k":
                        converted = (inp - 32)*0.5556+273.15
                        print(f"Converted value is {converted}")
                    else:
                        print("cannot convert, try again!(Check the units!)")
                        jlt()

                # length

                elif unit == "km":
                    if con == "m":
                        converted = inp*1000
                        print(f"Converted value is {converted}")
                    elif con == "cm":
                        converted = inp*100000
                        print(f"Converted value is {converted}")
                    elif con == "mm":
                        converted = inp*1000000
                        print(f"Converted value is {converted}")
                    elif con == "mi":
                        converted = inp/1.60934
                        print(f"Converted value is {converted}")
                    else:
                        print("cannot convert, try again!(Check the units!)")
                        jlt()
                elif unit == "mi":
                    if con == "km":
                        converted = inp*1.60934
                        print(f"Converted value is {converted}")
                    elif con == "m":
                        converted = inp*1609.34
                        print(f"Converted value is {converted}")
                    elif con == "cm":
                        converted = inp*160934
                        print(f"Converted value is {converted}")
                    elif con == "mm":
                        converted = inp*1609344
                        print(f"Converted value is {converted}")
                    else:
                        print("cannot convert, try again!(Check the units!)")
                        jlt()
                elif unit == "m":
                    if con == "mi":
                        converted = inp/1609.34
                        print(f"Converted value is {converted}")
                    elif con == "km":
                        converted = inp/1000
                        print(f"Converted value is {converted}")
                    elif con == "cm":
                        converted = inp*100
                        print(f"Converted value is {converted}")
                    elif con == "mm":
                        converted = inp*1000
                        print(f"Converted value is {converted}")
                    else:
                        print("cannot convert, try again!(Check the units!)")
                        jlt()
                elif unit == "cm":
                    if con == "mi":
                        converted = inp/160934
                        print(f"Converted value is {converted}")
                    elif con == "km":
                        converted = inp/100000
                        print(f"Converted value is {converted}")
                    elif con == "m":
                        converted = inp/100
                        print(f"Converted value is {converted}")
                    elif con == "mm":
                        converted = inp*10
                        print(f"Converted value is {converted}")
                    else:
                        print("cannot convert, try again!(Check the units!)")
                        jlt()
                elif unit == "mm":
                    if con == "mi":
                        converted = inp/1609344
                        print(f"Converted value is {converted}")
                    elif con == "km":
                        converted = inp/1000000
                        print(f"Converted value is {converted}")
                    elif con == "m":
                        converted = inp/1000
                        print(f"Converted value is {converted}")
                    elif con == "cm":
                        converted = inp/10
                        print(f"Converted value is {converted}")
                    else:
                        print("cannot convert, try again!(Check the units!)")
                        jlt()

                # mass(weight)

                elif unit == "kg":
                    if con == "lbs":
                        converted = inp*2.205
                        print(f"Converted value is {converted}")
                    elif con == "g":
                        converted = inp*1000
                        print(f"Converted value is {converted}")
                    else:
                        print("cannot convert, try again!(Check the units!)")
                        jlt()
                elif unit == "g":
                    if con == "lbs":
                        converted = inp*0.00220462
                        print(f"Converted value is {converted}")
                    elif con == "kg":
                        converted = inp/1000
                        print(f"Converted value is {converted}")
                    else:
                        print("cannot convert, try again!(Check the units!)")
                        jlt()
                elif unit == "lbs":
                    if con == "kg":
                        converted = inp/2.205
                        print(f"Converted value is {converted}")
                    elif con == "g":
                        converted = inp/0.00220462
                        print(f"Converted value is {converted}")
                    else:
                        print("cannot convert, try again!(Check the units!)")
                        jlt()

                # Currency

                elif unit == "d":
                    if con == "r":
                        converted = inp*80
                        print(f"Converted value is {converted}")
                    else:
                        print("cannot convert, try again!(Check the units!)")
                        jlt()
                elif unit == "r":
                    if con == "d":
                        converted = inp/80
                        print(f"Converted value is {converted}")
                    else:
                        print("cannot convert, try again!(Check the units!)")
                        jlt()

                # Done Finally

                else:
                    print("You entered an invalid unit!")
                    jlt()
            except ValueError:
                print("You entered the wrong value, please enter \"numbers only\"")
                jlt()
            again = input("Do you want to continue again?(y/n)/(yes/no): ").lower()
        elif again == "no" or again == "n":
            print("\nOKAY!\nProgram ended!")
        else:
            print("\nPlease type yes or no!!")
            jlt()
        break


jlt()