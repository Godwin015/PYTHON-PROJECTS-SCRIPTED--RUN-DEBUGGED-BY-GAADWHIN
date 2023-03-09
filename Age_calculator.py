#THIS PROGRAM WAS WRITTEN BY GAADWHIN TO CALCULATE THE ACTUAL AGE OF AN INDIVIDUAL
print("THIS PROGAM WAS SCRIPTED TO CALCULATE AGE, BIRTH YEAR AND CURRENT YEAR BY GAADWHIN")
print("NOTE THAT: to find Age, let Age be zero(0) when prompted and so on.")
Current_year = int(input("What year are we in? "))
Birth_year = int(input("What year were your born? "))
Age = int(input("How old are you? "))
choice = input("What do you want to calculate; Birth_year or Current_year or Age? ")
if choice == "Birth_year":
    born_year = Current_year - Age
    print("Your Birth year is " + str(born_year))
    print("Thanks for using Age_calculator BY Gaadwhin")
    input()
    exit()
elif choice == "Current_year":
    this_year = Birth_year + Age
    print("This current year is " + str(this_year))
    print("Thanks for using Age_calculator by Gaadwhin")
    input()
    exit()
elif choice == "Age":
    your_age = Current_year - Birth_year
    print("You are " + str(your_age) + " years old.")
    print("Thanks for using Age_calculator by Gaadwhin")
    input()
    exit()
else:
    print("SYNTAX ERROR!!!\n" + "WRONG INPUTS")
    print("Thanks for using Age_calculator by Gaadwhin")
    input()
    exit()
    