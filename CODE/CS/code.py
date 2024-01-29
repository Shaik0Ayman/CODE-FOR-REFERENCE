#perfect number
u=int(input("Enter upper range")) 
l=int(input("Enter lower range")) 
for i in range(l,u+1): 
sum1=0 
 
for j in range(1,i): 
if(i%j==0): 
sum1=sum1+j 
if(sum1==i): 
print(i) 

#ARMSTRONG NUMBER

u=int(input("Enter your upper limit")) 
l=int(input("Enter your lower limit")) 
for i in range(l,u+1): 
t=i 
l=len(str(i)) 
sum1=0 
while(i): 
a=i%10 
sum1=sum1+(a**l) 
i=i//10 
if(sum1==t): 
print(t) 

#PATTERN 
n=int(input("Enter the number of rows:")) 
for i in range(n): 
a=i+1 
b=n-1 
for j in range(i + 1): 
print(a," ",end="") 
a=a+b 
b=b-1 
print() 

#LINEAR AND BINARY SEARCH

def linear(n, list1): 
 
for i in range(len(list1)): 
if list1[i]==n: 
return i 
return -1 
 
 
 
 
def binary(n, list1): 
l=0 
u=len(list1)-1 
 
 
 
while l<=u: 
m=(l+u)//2 
 
 
if list1[m]<n: 
l=m+1 
elif list1[m]>n: 
u=m-1 
else: 
 
11 | P a g e  
return m 
return -1 
 
 
while True: 
 
 
 
ch=int(input('Enter choice 1.Linear search 2.Binary search : ')) 
list1=[] 
while True: 
 
a=input('Enter element: ') 
list1.append(a) 
 
 
ch1=input('Do you want to enter more y or n: ') 
if ch1 not in 'yY': 
break 
 
n=input('Enter string to search for: ') 
 
 
 
if ch==1: 
search=linear(n,list1) 
if search==-1: 
print ('Element not found') 
else: 
print ('Element found at index',search) 
 
 
 
elif ch==2: 
 
list1.sort() 
 
print ('Sorted list=', list1) 
search=binary(n,list1) 
if search==-1: 
 
print ('Element not found') 
else: 
 
Output: 
print ('Element found at index',search) 

#BUBBLE SORT 
def bubble_sort(List): 
for i in range(len(List)): 
for j in range(len(List)-i-1): 
if List[j][2] < List[j+1][2]: 
List[j], List[j+1] = List[j+1],List[j] 
repeat=1 
List=[] 
while repeat >0: 
details=input("Enter the DoctorId, Name, Specialization:") 
details=list(details.split(",")) 
List.append(details) 
cont=input("Do you want to continue(y/n):") 
if cont == "y": 
continue 
else: 
bubble_sort(List) 
print(List) 
break 

#INSERTION SORT

def insertion_sort(List): 
for i in List: 
j=List.index(i) 
while j>0: 
if int(List[j-1][3]) > int(List[j][3]): 
List[j-1],List[j] =List[j], List[j-1] 
else: 
break 
j=j-1 
repeat=1 
List=[] 
while repeat >0: 
details=str(input("Enter the Pid, Pname, Qty, Price:")) 
details=list(details.split(",")) 
List.append(details) 
print("Your data updated!!\n") 
cont=input("Do you want to continue(y/n):") 
if cont == "y": 
continue 
else: 
insertion_sort(List) 
print('Sorted list is ',List) 

#DISPLAY THE WORDS WITH LESS THAN 4 CHARACTERS IN A TEXT FILE
with open('Story.txt','w') as file: 
for i in range(5): 
a=input("Enter data") 
file.write(a+'\n') 
with open('Story.txt','r') as file: 
data=file.read() 
l=data.split() 
for i in l: 
if(len(i)<4): 
    
#COUNT THE NUMBER OF WORDS STARTING WITH A VOWEL IN A TEXT FILE 

with open('Book.txt','w') as file: 
for i in range(5): 
a=input("Enter data") 
file.write(a+'\n') 
def counter(): 
 
with open('Book.txt','r') as file: 
count=0 
data=file.read() 
l=data.split() 
for i in l: 
if(i[0] in 'AEIOUaeiou'): 
count=count+1 
print(count) 
counter()

#DISPLAY THE LINES WHICH END WITH “HEALTH” IN A TEXT FILE
with open('Exam.txt','w') as file: 
for i in range(5): 
a=input("Enter data") 
file.write(a+'\n') 
def display(): 
 
with open('Exam.txt','r') as file: 
while True: 
try: 
 
data=file.readline() 
l=data.split() 
if(l[len(l)-1]=='health'): 
print(data) 
except IndexError: 
break 
display()

#COUNT AND DISPLAY THE TOTAL NUMBER OF WORDS THAT STARTS WITH A VOWEL IN A TEXT FILE
with open('Book.txt','w') as file: 
for i in range(5): 
a=input("Enter data") 
file.write(a+'\n') 
def counter(): 
 
with open('Book.txt','r') as file: 
count=0 
data=file.read() 
l=data.split() 
for i in l: 
if(i[0] in 'AEIOUaeiou'): 
count=count+1 
print(i) 
print(count) 
counter() 

#WRITE AND READ A BINARY FILE 
import pickle 
 
ch=int(input("What do you want to do 1.Add information 2.Display cars with name 
toyota")) 
if(ch==1): 
 
with open('CARS.dat','wb') as file: 
flag='y' 
while(flag=='y'): 
carno=int(input("Enter car number")) 
carname=input("Enter car name") 
mileage=int(input("Enter mileage")) 
price=int(input("Enter price")) 
l=[carno,carname,mileage,price] 
pickle.dump(l,file) 
a=input("Do you want to enter more data yes or no") 
if(a=='yes'): 
flag='y' 
else: 
flag='n' 
break
def reader(): 
 
print("Displaying cars with name as toyota") 
with open('CARS.dat','rb') as file: 
while True: 
try: 
data=pickle.load(file) 
if(data[1]=='Toyota'): 
print("Carname:",data[1],"Price:",data[3]) 
except EOFError: 
break 
 
reader()

#UPDATE A BINARY FILE   
import pickle 
def write(): 
with open("Mobile.dat",'wb') as file: 
flag='y' 
while(flag=='y'): 
modelno=int(input("Enter modelno")) 
memorycard=input("Enter memorycard storage details") 
megapixel=int(input("Enter megapixel")) 
l=[modelno,memorycard,megapixel] 
pickle.dump(l,file) 
a=input("Do you want to enter more data yes or no") 
if(a=='yes'): 
flag='y' 
else: 
flag='n' 
break 
write() 
def upd(): 
with open("Mobile.dat",'rb+') as file: 
modelno=int(input("Enter the modelnumber you want to update ")) 
megapix=int(input("Enter new megapixel")) 
l=[] 
while True: 
try: 
data=pickle.load(file) 
if data[0]==modelno: 
data[2]=megapix 
l.append(data) 
else: 
l.append(data) 
except EOFError: 
break 
for i in l: 
pickle.dump(i,file) 
if(i[0]==modelno): 
print(i) 
print("Data updated") 
upd()

#WRITE ,DELETE AND COUNT THE NUMBER OF RECORDS IN A BINARY FILE
import pickle 
 
ch=int(input("What do you want to do 1.Enter information 2.Delete records 3.View 
records")) 
if(ch==1): 
def write(): 
with open("Telephone.dat",'wb') as file: 
flag='y' 
while(flag=='y'): 
name=input("Enter your name") 
address=input("Enter your address") 
areacode=int(input("Enter areacode")) 
phonenumber=int(input("Enter phone number")) 
l=[name,address,areacode,phonenumber] 
pickle.dump(l,file) 
a=input("Do you want to enter more data yes or no") 

if(a=='yes'): 
flag='y' 
else: 
 
flag='n' 
break 
write() 
elif(ch==2): 
def dele(): 
 
with open("Telephone.dat",'rb') as file: 
area=int(input("Enter the areacode you want to delete")) 
l=[] 
while True: 
try: 
data=pickle.load(file) 
if(data[2]!=area): 
l.append(data) 
except EOFError: 
break 
 
with open("Telephone.dat",'wb') as file: 
for i in l: 
pickle.dump(i,file) 
print("Record deleted") 
dele() 
elif(ch==3): 
 
def read(): 
 
with open("Telephone.dat",'rb') as file: 
count=0 
while True: 
try: 
data=pickle.load(file) 
print(data) 
count=count+1 
except EOFError: 
break 
print("Total records:",count) 
read()

#CSV FILE -READING , WRITING AND DISPLAYING 
import csv 
ch=int(input("Enter your choice 1.Write 2.Display records with average more than the 
minimum value")) 
def write(): 
with open ('student.csv','w',newline='') as file: 
wri=csv.writer(file) 
c=1 
while(c==1) : 
rno=int(input('Enter roll number: ')) 
name=input('Enter name: ') 
m1=float(input('Enter mark 1: ')) 
m2=float(input('Enter mark 2: ')) 
m3=float(input('Enter mark 3: ')) 
m4=float(input('Enter mark 4: ')) 
m5=float(input('Enter mark 5:' )) 
avg=(m1+m2+m3+m4+m5)/5 
row=[rno, name, m1, m2, m3, m4, m5, avg] 
wri.writerow(row) 
ch2=input('Continue? (y/n): ') 
 
 
if(ch2 =='n'): 
c=2 
break
def read(): 
with open('student.csv','r') as file: 
av=int(input("The minimum average mark")) 
print("Students who have average above ",av,"are") 
r=csv.reader(file) 
for i in r: 
if(float(i[7])>av): 
print("Rollno:",i[0]) 
print("Name:",i[1]) 
print("Mark1:",i[2]) 
print("Mark2:",i[3]) 
print("Mark3:",i[4]) 
print("Mark4:",i[5]) 
print("Mark5:",i[6]) 
print("Avg:",i[7]+"\n") 
 
 
 
if(ch==1): 
write() 
elif(ch==2): 
read()

#SUM OF BOUNDARY, NON-BOUNDARY, RIGHT AND LEFT DIAGONAL ELEMENTS OF A NESTED LIST 
n=int(input("Enter number of rows:")) 
l=[] 
for i in range(n): 
l1=[] 
for j in range(n): 
ele=int(input("Enter element")) 
l1.append(ele) 
l.append(l1) 
print("Your matrix is:") 
for i in l: 
print(i) 
 
 
 
sum1=0 
 
for i in range(len(l)): 
if(i==0 or i==(len(l)-1)): 
for j in l[i]: 
sum1=sum1+j 
else: 
for j in range (len(l[i])): 
if(j==0 or j==(len(l[i])-1)): 
sum1=sum1+l[i][j] 
 
print("Sum of boundary elemnets:",sum1) 
total=0 
for i in l: 
for j in i: 
total=total+j 
non=total-sum1 
print("Sum of non-boundary elements:",non) 
tot=0 
for i in range(len(l)): 
tot=tot+l[i][i] 
print("Sum of right diagonal elements:",tot) 
tot1=0 
for i in range(len(l)): 
tot1=tot1+l[i][len(l[i])-i-1] 
print("Sum of left diagonal elements:",tot1)

#STACK OPERATIONS USING LIST
l=[] 
 
def push(): 
 
custid=int(input("Enter customer id")) 
custname=input("Enter customer name") 
phone=int(input("Enter phone number")) 
lis=custid,custname,phone 
l.append(lis) 
 
print("Record has been added") 
print(l) 
def popfun(): 
if(l==[]): 
print("Stack is empty") 
else: 
l.pop() 
def show(): 
if(l==[]): 
print("empty stack") 
else:
for i in l: 
print(i) 
 
 
while True: 
 
choice=int(input('What do you want to do:(1)push(2)pop(3)display(4)break')) 
if choice == 1: 
push() 
 
elif choice == 2: 
popfun() 
elif choice == 3: 
show() 
elif choice==4:
break
