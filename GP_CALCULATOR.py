print("GP CALCULATOR BY GAADWHIN")
print("NOTE: select the accurate range to get the best results")
name = input("InPuT yOuR nAmE: \n")
print("NOTE: 40-44= 2.0 \n45-49= 2.25 \n50-54= 2.50 \n55-59= 2.75 \n60-64= 3.0 \n65-69= 3.25 \n70-74= 3.50 \n75-100= 4.0 ")
course_1 = float(input("Select range for course 1\n"))
course_1_credit_unit = float(input("what is the credit unit: \n"))
a = course_1 * course_1_credit_unit
course_2 = float(input("Select range for course 2\n"))
course_2_credit_unit = float(input("what is the credit unit: \n"))
b = course_2 * course_2_credit_unit
course_3 = float(input("Select range for course 3\n"))
course_3_credit_unit = float(input("what is the credit unit: \n"))
c = course_3 * course_3_credit_unit
course_4 = float(input("Select range for course 4\n"))
course_4_credit_unit = float(input("what is the credit unit: \n"))
d = course_4 * course_4_credit_unit
course_5 = float(input("Select range for course 5\n"))
course_5_credit_unit = float(input("what is the credit unit: \n"))
e = course_5 * course_5_credit_unit
course_6 = float(input("Select range for course 6\n"))
course_6_credit_unit = float(input("what is the credit unit: \n"))
f = course_6 * course_6_credit_unit
course_7 = float(input("Select range for course 7\n"))
course_7_credit_unit = float(input("what is the credit unit: \n"))
g = course_7 * course_7_credit_unit
course_8 = float(input("Select range for course 8\n"))
course_8_credit_unit = float(input("what is the credit unit: \n"))
h = course_8 * course_8_credit_unit
course_9 = float(input("Select range for course 9\n"))
course_9_credit_unit = float(input("what is the credit unit: \n"))
i = course_9 * course_9_credit_unit
course_10 = float(input("Select range for course 10\n"))
course_10_credit_unit = float(input("what is the credit unit: \n"))
j = course_10 * course_10_credit_unit
total_grade = float(a) + float(b) + float(c) + float(d) + float(e) + float(f) + float(g) + float(h) + float(i) + float(j)
total_credit_unit = float(course_1_credit_unit) + float(course_2_credit_unit) + float(course_3_credit_unit) + float(course_4_credit_unit) + float(course_5_credit_unit) + float(course_6_credit_unit) + float(course_7_credit_unit) + float(course_8) * float(course_8_credit_unit) + float(course_9_credit_unit) + float(course_10_credit_unit)
G_P = float(total_grade) / float(total_credit_unit)
if G_P < float(2.5):
    print(name + ", your G.P is " + str(G_P) + " PASS, " + "You need to be more Serious with your studies")
    print("Thanks for using GP Calculator by GAADWHIN")
    input()
    exit()
elif G_P <float(3.0):
    print(name + ", your G.P is " + str(G_P) + " LOWER CREDIT, " + " Put more effort, You can do better next Semester")
    print("Thanks for using GP Calculator by GAADWHIN")
    input()
    exit()
elif G_P < float(3.4):
    print(name + ", your G.P is " + str(G_P) + " UPPER CREDIT, " + " Good Grade, Keep it up! Distinction is only a step ahead")
    print("Thanks for using GP Calculator by GAADWHIN")
    input()
    exit()
elif G_P > float(3.5):
    print(name + ", your G.P is " + str(G_P) + " DISTINCTION, " + " Excellent Grade, no be lie your results make sense die!")
    print("Thanks for using GP Calculator by GAADWHIN")
    input()
    exit()
else:
    print("This Result Choke")
    print("Thanks for using GP Calculator by GAADWHIN")
    input()
    exit()