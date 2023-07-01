#NOTE THAT THIS CALCULATOR WAS SCRIPTED TO CALCULATE ONLY ADDITION, SUBSTRACTION, DIVISION AND MULTIPLICATION
print("SIMPLE CALCULATOR SCRIPTED BY GAADWHIN")
name = input("What is your name? ")
first_number = int(input("input the first figure: "))
second_number = int(input("input the second figure: "))
choice = input("What function do you want to perform\nAdditon or Substraction or Division or Multiplication? ")
if choice == "Addition":
    Added = first_number + second_number
    print(str(name) + ", the Addition of first and second figure is " + str(Added))
    print("Thank you for using my_calculator by Gaadwhin")
    input()
    exit()
elif choice == "Substraction":
    Substracted = first_number - second_number
    print(str(name) + ", the Substraction of first and second figure is " + str(Substracted))
    print("Thank you for using my_calculator by Gaadwhin")
    input()
    exit()
elif choice == "Division":
    Divided = first_number / second_number
    print(str(name) + ", the Division of first and second figure is " + str(Divided))
    print("Thank you for using my_calculator by Gaadwhin")
    input()
    exit()
elif choice == "Multiplication":
    Multiplied = first_number * second_number
    print(str(name) + ", the Multiplication of first and second figure is " + str(Multiplied))
    print("Thank you for using my_calculator by Gaadwhin")
    input()
    exit()
else:
    print("syntax error!\n" + "WRONG INPUT")
    print("Thank you for using my_calculator by Gaadwhin")
    input()
    exit()
