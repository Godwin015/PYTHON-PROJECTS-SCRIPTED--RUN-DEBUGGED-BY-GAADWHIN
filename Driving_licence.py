name = input("What is your name? ")
age = int(input("How old are you? "))
purpose = str(input("Do you want to apply for a driving license?\n "))

if age >= 18 and purpose == "yes":
    print(name + ", You are eligible to apply for a driving license!")
    print("Proceed to make all necessary payments at https://www.abdcef.com")
    print("Thanks for using Driving license by Gaadwhin")
    input()
    exit()
elif age >= 18 and purpose == "no":
    choice = input("What task for do you want to perform?\n")
    print(name + ", " + choice + " DOES NOT EXIST IN THIS DATABASE")
    print("Thanks for using Driving license by Gaadwhin")
    input()
    exit()
elif age < 18 and purpose == "yes":
    print(name + ", You are not eligible to apply for a driving license!")
    input()
    exit()
elif age < 18 and purpose == "no":
    choice = input("What task for do you want to perform?\n")
    print(name + ", " + choice + " DOES NOT EXIST IN THIS DATABASE")
    print("Thanks for using Driving license by Gaadwhin")
    input()
    exit()
else:
    print(name + ", You are not eligible to apply for a driving license!")
    input()
    exit()
