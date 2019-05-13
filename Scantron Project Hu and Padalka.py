##CMPT 120        
##Final Project - Processing Data
##Instructor: Diana Cukierman
##Authors: Sergii Padalka and Tim Hu
##Saturday, 2nd December, 2017

###---Global Variables---###
answerList=[] #from IN_key+pts.txt
dataList=[] #from IN_data_studs.txt
numStudents=0 
numQuestions=0
ansKey="" 
numToLetter="" #correct answer in the form of a letter
stPartialAnswerList="" #string of points for each question
pointList = [] #list of points for each question
startSearch = 0 #point of start for finding the numbers in stPartialAnswerList
maxPoints=0 #maximum points possible in total
keyList=[] #answer key
resList=[]
resResList=[] #List of lists of results (i.e. resList)
namesList=[]
maximal=0
studentAccu=[] #accuracy of all students
allScore=[]
percList=[]
studentMark=[] #accuracy of all students grouped
studentsSelected=[]
listForCSV=[]
ansCorrectList=[] #number of times each question was answered correctly
hardList=[]
distrList=[]
gradeList=[]
upperBound=0 #closest number in the tens greater than the percentage

###Provided functions###
def read_string_list_from_file(the_file): #by Diana Cukierman
    fileRef = open(the_file,"r") 
    localList=[]
    print("FILEREF",fileRef)
    for line in fileRef:
        string = line[0:len(line)-1]                             
        localList.append(string)                               
    fileRef.close()  
    print ("\n JUST TO TRACE, the local list of strings is:\n")
    for element in localList:
        print (element) 
    return localList

def write_result_to_file(lres,the_file): #by Diana Cukierman
    fileRef = open(the_file,"w")
    for line in lres:
        fileRef.write(line)                                   
    fileRef.close()
    return

###Mandatory Programmers' functions###
def average(List):
    total=0
    for i in studentsSelected:
        total+=List[i]
    avg=0
    avg=total/len(studentsSelected)
    return avg

def cleanList(emptyList,length,form):
    for i in range (length):
        if form=="number": 
            emptyList.append(0)
        elif form=="text":
            emptyList.append("")
    return emptyList

def farewell():
    print("Thank you for using the program. Have a nice day!")
    return
        
def listOfListMaker(emptyList,start,stop,loopRange,sourceList,separPoint):
    for i in range (loopRange):
        emptyList.append(sourceList[start:stop])
        start=stop
        stop=stop+separPoint
    return emptyList

def maximum(List):
    maximal=0
    for i in studentsSelected:
        if List[i]>maximal:
            maximal=List[i]
    return maximal

def minimum(list1, list 2, ):
    minimal=numStudents
    for i in range (len(ansCorrectList)):
        if List[i]<minimal:
            minimal=List[i]
    return minimal

def separators(length):
    for i in range (length):
        print("--------------------",end="")
    print()
    return

def validRepeat(choice, options):
    while choice not in options:
        choice=input("Please try again: ")
    return choice

###Optional Functions###
def graph(List):
    t.Screen().colormode(255)
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-200,-200)
    t.pendown()
    t.begin_fill()
    t.fillcolor(50,205,50)
    for i in List:
        t.forward(20)
        t.left(90)
        t.forward(i*50)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(i*50)
        t.left(90)
    t.left(180)
    t.forward(20*len(List)*2)
    t.end_fill()
    return
#----------<<<<<Top Level>>>>>----------#
import math as m
import turtle as t

answerList=read_string_list_from_file("IN_key+pts.txt")
separators(3)
dataList=read_string_list_from_file("IN_data_studs.txt")
##print("TRACE ANSWERS:", answerList)
##print("TRACE DATA:", dataList)

#Welcome
separators(4)
print("Hello and welcome to the Scantron Workatron!\
      \n(~Copyright Canadian-Caribbean Educational Initiative 2017~)")
separators(4)

#Output the number of students
for i in range (len(dataList)):
    numStudents+=1
print ("The number of students is", numStudents)

#Output the number of questions
for i in range (len(answerList[0])):
    numQuestions+=1
print ("The number of questions is", numQuestions)
print()

#Output the answer key
for i in range (numQuestions):
    if answerList[0][i]=='1':
        numToLetter="A"
    elif answerList[0][i]=='2':
        numToLetter="B"
    elif answerList[0][i]=='3':
        numToLetter="C"
    elif answerList[0][i]=='4':
        numToLetter="D"
    elif answerList[0][i]=='5':
        numToLetter="E"
    else:
        print ("Perform percussive maintenance on scantron")
    ansKey+=numToLetter+" "
print ("The answer key is:\n",ansKey)

#Output the max points for all questions in a line
print ("The maximum points possible for every question are:\n", answerList[1])
print()

#Output total points possible
for i in range (len(answerList[1])):
    stPartialAnswerList+=answerList[1][i]
stPartialAnswerList+=" "
##print ("TRACE stPartialAnswerList:",stPartialAnswerList)


for i in range(numQuestions):
    spaceIndex=stPartialAnswerList.find(" ",startSearch)
    ##print("TRACE spaceIndex:", spaceIndex)
    pointList.append(float(stPartialAnswerList[startSearch:spaceIndex]))
    ##print("TRACE pointList:", pointList)
    startSearch = spaceIndex + 1
    ##print("TRACE startSearch:", startSearch)
##print ("TRACE pointList:", pointList)

for i in (range(len(pointList))):
    maxPoints+=pointList[i]
print ("The maximum points possible in total are:", maxPoints)
print ()

for i in range (numQuestions):
    keyList.append(answerList[0][i])
##print ("TRACE keyList:", keyList)

i=0
startComparison=0
while i<(numStudents):
    j=0  
    while j<(len(dataList[i])) and not dataList[i][j].isdigit():
        j+=1
    startComparison=j
    while j<(len(dataList[i])):
        resList.append(dataList[i][j])
        j+=1
    i+=1
##print("TRACE resList:",resList)
    
resResList=listOfListMaker(resResList,0,numQuestions,numStudents,resList,numQuestions)
##print("TRACE resResList:",resResList)

#Getting names of students
for i in range (numStudents):
    names=""
    j=0
    while j<(len(dataList[i])) and dataList[i][j].isalpha():
        names+=dataList[i][j]
        j+=1
    namesList.append(names)
##print ("TRACE namesList:", namesList)
##print()

#Marking the students; Max Points; Recording right&wrong answers; Record All
#students' marks; Record percentages

for lists in resResList:
    score=0
    percent=0
    for i in range(len(lists)):
        if lists[i]==answerList[0][i]:
            score+=pointList[i]
            studentAccu.append(1)
        else:
            studentAccu.append(0)
        percent= round(((score/maxPoints)*100),1)

    allScore.append(score)
    percList.append(percent)
##print("TRACE studentAccu:", studentAccu)
##print("TRACE allScore:", allScore)
##print("TRACE percList:", percList)

studentMark=listOfListMaker(studentMark,0,numQuestions,numStudents,studentAccu,numQuestions)
##print("TRACE studentMark:",studentMark)

separators(4)
#Ask the user for input to process the whole class or process selected students
print("Type ALL if you would like to process the whole class\
      \nType SEL to process certain students (up to half of the whole class)")
print()
amtToProcess=input("Would you like to process the whole class or select students?: ")
amtToProcess=validRepeat(amtToProcess, ['ALL','All','all','SEL','Sel','sel'])
print()

#Limiting the number of students to process
if amtToProcess in ['SEL','Sel','sel']:
    terminate=False
    i=0
    while i<(numStudents//2) and terminate==False:
        studentToProcess=input("Please enter a student's name or type END to finish: ")
        while (studentToProcess not in namesList) and (studentToProcess not in ["END","End","end"]):
            studentToProcess=input("Please try again: ")
        if studentToProcess in ["END","End","end"]:
            terminate=True
        else:
            studentPos=namesList.index(studentToProcess)
            print("Student", studentToProcess, "obtained", allScore[studentPos], "points")
            studentsSelected.append(studentPos)
        i+=1
        if i==(numStudents//2):
            print("You have reached your limit for selecting students.\
                  \nYou cannot select more than half of the total")
##    print(studentsSelected)
    numStudents=len(studentsSelected)
##    print("TRACE numStudents:", numStudents)
if numStudents==0:
    print("There are no students to process. No data will therefore be generated.\
          \nThank you for using this program. Have a nice day!")
    quit()
if amtToProcess in ['ALL','All','all']:
    for i in range (numStudents):
        studentsSelected.append(i)
##    print (studentsSelected)
    
    
#Printing scores for each
print("Here are the results:")
print()

for i in studentsSelected:
    listForCSV.append('"'+namesList[i]+'"'+","+str(allScore[i])+"," +str(percList[i])+"\n")
##print (listForCSV)
for i in range (len(listForCSV)):
    print (listForCSV[i])
write_result_to_file(listForCSV,"OUT_results.csv")

#-----(Statistics)-----#
separators(4)
print("Statistics:")
print()
#Maximum points
print("Maximum number of points achieved:", maximum(allScore))
print()

#Average marks            
print("The average score is:", average(allScore),"or", average(percList),"%")
print()

#Number of students processed
print("Number of students processed:", numStudents)
print()

#Questions answered correctly
ansCorrectList=cleanList(ansCorrectList,numQuestions,"number")
for i in studentsSelected:
    for j in range (len(studentMark[i])):
        if studentMark[i][j]==1:
            ansCorrectList[j]+=1

print("Number of times each question was answered correctly:")
print(ansCorrectList)
print()

#Hardest questions
for i in range(len(ansCorrectList)):
    if ansCorrectList[i]==minimum(ansCorrectList):
        hardList.append(i+1)

print("Most difficult questions:", hardList)
print()

#Making a list of zeroes
distrList=cleanList(distrList,10,"number")
##print("TRACE distrList:", distrList)

#Making a list for grades, the fancy way
grade=0
for i in range(10):
    grade+=10
    gradeList.append(grade)
##print("TRACE gradeList:", gradeList)

#Distribution of points
for i in studentsSelected:
    upperBound=(m.ceil(percList[i]/10))*10
    gradeIndex=gradeList.index(upperBound)
    distrList[gradeIndex]+=1
print("Distribution of points:", distrList)
print("(With respect to:", gradeList,")")
print()

#-----(OPTIONAL SECTION)-----#
#Turtle Drawing
separators(4)
graphOption=input("Would you like to see a histogram of the distribution of points? (Y/N): ")
graphOption=validRepeat(graphOption, ['Y','N','y','n'])

if graphOption in ['Y','y']:
    graph(distrList)

#Calculate distance
userAnswer=input("Would you like to do calculate the distance between two questions? (Y/N): ")
userAnswer=validRepeat(userAnswer, ['Y','N','y','n'])
print()
if userAnswer in ['N','n']:
    print("Thank you for using the program. Have a nice day!")
while userAnswer in ['Y','y']:
    print("Please note, an input of 0 for the first question will terminate the program")
    print()
    dis=input("Input first question's number: ")
    while not dis.isdigit():
        print()
        dis=input("What you typed is not an integer, please try again \nFirst Question: ")
    if int(dis)==0:
        print("Thank you for using the program. Have a nice day!")
        break
    dis2=input("And the second one: ")
    while not dis.isdigit() or not dis2.isdigit():
        print()
        dis=input("What you typed are not intergers, please try again \nFirst Question: ")
        dis2=input("And the second one as well \nSecond Question: ")
    while int(dis2) == 0 or int(dis)>numQuestions or int(dis2)>numQuestions:
        print()
        dis=input("The value is out of range, please try again \nFirst Question: ")
        dis2=input("And the second one as well \nSecond Question: ")
    print()
    
#Since it starts counting at zero, make value one less than the user input                   
    dis=int(dis)-1
    dis2=int(dis2)-1
    acc=0
    for i in range(len(studentMark)):
##        print(studentMark[i])
        if studentMark[i][dis]!=studentMark[i][dis2]:
##           print("TRACE studentMark[i][dis],studentMark[i][dis2]:",\
##                  studentMark[i][dis],studentMark[i][dis2])
            acc+=1
    if acc==0:
        print("There is no distance between the two values")
        print()
    else:
        print("The distance between questions "+ str(dis+1) + \
               " and " + str(dis2+1) + " is " + str(acc))
        print()
    userAnswer=input("Would you like to try another distance calculation? (Y/N): ")
    userAnswer=validRepeat(userAnswer, ['Y','N','y','n'])
    print()
    if userAnswer in ['N','n']:
        farewell()
