print("WELCOME TO EXAMINATION RESULT SIMULATION SCRIPTED BY GAADWHIN")
print("INPUT ONLY ACCURATE DETAILS TO GET THE ACCURATE RESULTS")

name = input("Input your name: ")
Registration_number = input("Input your Registration Number: ")

Godwin_result = "\nENG A1\nMTH B3\nCHEM B2\nBIO A1\nPHY A1\nAGRIC B2"
Edwin_result = "\nENG B3\nMTH A1\nCHEM B2\nBIO B3\nPHY C4\nC.R.S A1"
Erwin_result = "\nENG B2\nMTH C5\nLIT. B2\nGEO B2\nECONS A1\nMRKT B3"

if name == "Godwin" and Registration_number == "86303258AH":
    print("Result for: " + name + "\nRegistration number: " + Registration_number + " is" + Godwin_result)
    print("Thanks for using Examination Result Simulation by GAADWHIN")
    input()
    exit()
elif name == "Edwin" and Registration_number == "86303258AH":
    print("Result for: " + name + "\nRegistration number: " + Registration_number + " is" + Edwin_result)
    print("Thanks for using Examination Result Simulation by GAADWHIN")
    input()
    exit()
elif name == "Erwin" and Registration_number == "86303258AH":
    print("Result for: " + name + "\nRegistration number: " + Registration_number + " is" + Erwin_result)
    print("Thanks for using Examination Result Simulation by GAADWHIN")
    input()
    exit()
else:
    print("WRONG DETAILS\nCHECK NAME AND REGISTRATION NUMBER AGAIN")
