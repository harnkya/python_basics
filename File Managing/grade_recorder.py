def calculate_average(line):
    line=line[:-1]
    list=line.split(":")
    student=list[0]
    marks=list[1].split(',')
    grade1=int(marks[0])
    grade2=int(marks[1])
    grade3=int(marks[2])
    average=(grade1+grade2+grade3)/3
    letter=""
    
    if average>=90 and average<=100:
        letter ="AA"
    elif average>=85 and average<=89:
        letter="BA"
    elif average>=80 and average<=84:
        letter="BB"
    elif average>=75 and average<=79:
        letter="CB"
    elif average>=65 and average<=74:
        letter="CC"
    elif average >=60 and average <=64:
        letter="DC"
    elif average >=55 and average<=59:
        letter="DD"
    elif average>=50 and average<=54:
        letter="FD"
    else:
        letter="FF"

    return student + ":" +letter+ "\n"




def read_grades():
    with open("grades.txt","r",encoding="utf-8") as file:
        for line in file:
            print(calculate_average(line))

def enter_mark():
    name=input("student name: ")
    secondname=input("student secondname: ")
    grade1=input("first grade: ")
    grade2=input("second grade: ")
    grade3=input("third grade: ")

    with open("grades.txt","a",encoding="utf-8") as file:
        file.write(name+" "+secondname+": " +grade1+","+grade2+","+grade3 +"\n")


def record_mark():
    with open("marks.txt","r",encoding="utf-8")as file:
        list=[]

        for i in file:
            list.append(calculate_average(i))

        with open("results.txt","w",encoding="utf-8") as file2:
            for i in file2:
                file2.write(i)

while True:
    activity=input("Please select the process:\n1-show marks\n2-enter grade\n3-record grades\n4-exit\n")

    if activity=="1":
        read_grades()
    elif activity=="2":
        enter_mark()
    elif activity=="3":
        record_mark()
    else :
        break
  
    
