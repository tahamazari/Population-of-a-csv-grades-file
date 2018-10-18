import csv
import random

def avg(s1, s2, s3, s4, s5, s6, s7, s8):
    sum = 0
    category = ''

    #Subject 1
    if(s1 == 0):
        sum += 90
    else:
        sum += 85 -(10*(s1-1))

    #Subject 2
    if(s2 == 0):
        sum += 90
    else:
        sum += 85 -(10*(s2-1))

    #Subject 3
    if(s3 == 0):
        sum += 90
    else:
        sum += 85 -(10*(s3-1))

    #Subject 4
    if(s4 == 0):
        sum += 90
    else:
        sum += 85 -(10*(s4-1))

    #Subject 5
    if(s5 == 0):
        sum += 90
    else:
        sum += 85 -(10*(s5-1))

    #Subject 6
    if(s6 == 0):
        sum += 90
    else:
        sum += 85 -(10*(s6-1))

    #Subject 7
    if(s7 == 0):
        sum += 90
    else:
        sum += 85 -(10*(s7-1))

    #Subject 8
    if(s8 == 0):
        sum += 90
    else:
        sum += 85 -(10*(s8-1))

    sum = sum/8

    if(sum >= 90):
        category = 'Excellent'
    elif(sum >= 80):
        category = 'Very Good'
    elif(sum >= 70):
        category = 'Good'
    elif(sum >= 60):
        category = 'Average'
    elif(sum >= 50):
        category = 'Poor'
    elif(sum < 50):
        category = 'Fail'

    return(category)


myData = [["Physics A*","Physics A","Physics B","Physics C","Physics D","Physics E",
           "Maths A*", "Maths A", "Maths B", "Maths C", "Maths D", "Maths E",
           "Urdu A*", "Urdu A", "Urdu B", "Urdu C", "Urdu D", "Urdu E",
           "English A*", "English A", "English B", "English C", "English D", "English E",
           "Chemistry A*", "Chemistry A", "Chemistry B", "Chemistry C", "Chemistry D", "Chemistry E",
           "Biology A*", "Biology A", "Biology B", "Biology C", "Biology D", "Biology E",
           "Pak Stud. A*", "Pak Stud. A", "Pak Stud. B", "Pak Stud. C", "Pak Stud. D", "Pak Stud. E",
           "Islamiat A*", "Islamiat A", "Islamiat B", "Islamiat C", "Islamiat D", "Islamiat E",
           "Class"]]

for i in range(60):
    a = random.randrange(0, 6, 1)
    b = random.randrange(0, 6, 1)
    c = random.randrange(0, 6, 1)
    d = random.randrange(0, 6, 1)
    e = random.randrange(0, 6, 1)
    f = random.randrange(0, 6, 1)
    g = random.randrange(0, 6, 1)
    h = random.randrange(0, 6, 1)

    temp = []
    for j in range(6):
        if(j == a):
            temp.append(1)
        else:
            temp.append(0)
    for j in range(6):
        if(j == b):
            temp.append(1)
        else:
            temp.append(0)
    for j in range(6):
        if(j == c):
            temp.append(1)
        else:
            temp.append(0)
    for j in range(6):
        if(j == d):
            temp.append(1)
        else:
            temp.append(0)
    for j in range(6):
        if(j == e):
            temp.append(1)
        else:
            temp.append(0)
    for j in range(6):
        if(j == f):
            temp.append(1)
        else:
            temp.append(0)
    for j in range(6):
        if(j == g):
            temp.append(1)
        else:
            temp.append(0)
    for j in range(6):
        if(j == h):
            temp.append(1)
        else:
            temp.append(0)


    temp.append(avg(a,b,c,d,e,f,g,h))
    myData.append(temp)

myFile = open('task_1.csv', 'w', newline='')
with myFile:
   writer = csv.writer(myFile)
   writer.writerows(myData)
