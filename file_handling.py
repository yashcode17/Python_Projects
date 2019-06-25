import os

#to create folder in desktop
print(os.getcwd())
os.chdir(r"C:\Users\HP\Desktop")
if(os.path.isdir("student_data")):
    print("already exists")
else:
    os.mkdir("student_data")
    print("folder created")

os.chdir(r"C:\Users\HP\Desktop\student_data")

if(os.path.isdir("student_name")):
    print("already exists")
else:
    os.mkdir("student_name")
    print("folder created")

# os.mkdir("student_name")
if(os.path.isdir("student_record")):
    print("already exists")
else:
    os.mkdir("student_record")
    print("folder created")

# os.mkdir("student_record")
os.chdir(r"C:\Users\HP\Desktop\student_data\student_name")

a=open("name.txt","w")
a.write("1.yashasvi "
        "2.shuchita "
        "3.pahul ")
a.close()
os.chdir(r"C:\Users\HP\Desktop\student_data\student_record")
a=open("record.txt","w")
a.write("11701150 "
        "11701085 "
        "11701144 ")
a.close()

# to create scv file

a=open("myfile.csv","w")
a.write("id,name,salary,city \n")
a.write("1,A,1000,chd")
a.close()

a=open("record.txt","r")
data=a.read
print(data)
a.close()


