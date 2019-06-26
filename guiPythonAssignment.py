import mysql.connector
import tkinter as t

connection=mysql.connector.connect(
    host='localhost',
    user="root",
    password="**********"
)

sql = connection.cursor()

def createdb(dbname):
    query="CREATE DATABASE IF NOT EXISTS "+dbname
    sql.execute(query)
    print("database created")

createdb("loginData")
sql.execute("use loginData")

def createtb(tbname):
    query="CREATE TABLE IF NOT EXISTS "+tbname+"(name varchar(30),city varchar(30),mobile varchar(50),email varchar(50) primary key,password varchar(30),gender varchar(10),course varchar(30))"
    sql.execute(query)
    print("table created")

createtb("loginDataTable")

root=t.Tk()
root.state("zoomed")

lable1=t.Label(root,text="Name")
lable1.grid(padx=100,pady=10,column=0,row=0)
textbox1=t.Entry(root)
textbox1.grid(column=1,row=0)

lable2=t.Label(root,text="City")
lable2.grid(column=0,row=1,pady=10)
textbox2=t.Entry(root)
textbox2.grid(column=1,row=1)

lable3=t.Label(root,text="Phone No.")
lable3.grid(column=0,row=2,pady=10)
textbox3=t.Entry(root)
textbox3.grid(column=1,row=2)

lable4=t.Label(root,text="Email")
lable4.grid(column=0,row=3,pady=10)
textbox4=t.Entry(root)
textbox4.grid(column=1,row=3)

# # lable4=t.Label(root,text="Email")
# # lable4.grid(column=0,row=3)
# # textbox4=t.Entry(root)
# # textbox4.grid(column=1,row=3)
# # email=textbox4.get()
#
lable5=t.Label(root,text="Password")
lable5.grid(column=0,row=4,pady=10)
textbox5=t.Entry(root,show="*")
textbox5.grid(column=1,row=4)

lable6=t.Label(root,text="Gender")
lable6.grid(column=0,row=5,pady=10)

v1=t.IntVar()
r1=t.Radiobutton(root,text="Female",variable="v1",value=1)
r1.grid(column=1,row=5)
r2=t.Radiobutton(root,text="Male",variable="v1",value=2)
r2.grid(column=2,row=5)

lable7=t.Label(root,text="Course")
lable7.grid(column=0,row=6,pady=10)
c1=t.IntVar()
c2=t.IntVar()
c3=t.IntVar()
d1=t.Checkbutton(root,text="Java",variable=c1)
d1.grid(column=1,row=6)
d2=t.Checkbutton(root,text="PHP",variable=c2)
d2.grid(column=2,row=6)
d3=t.Checkbutton(root,text="Python",variable=c3)
d3.grid(column=3,row=6)

def submitForm():
    nameu = textbox1.get()
    cityu = textbox2.get()
    phoneNou = textbox3.get()
    emailu = textbox4.get()
    passwordu = textbox5.get()
    if v1.get()==1:
        genderu="female"
    else:
        genderu="male"

    print(nameu)

    if c1.get()==1 and c2.get()==1 and c3.get()==1:
        courseu = "Java/PHP/Python"
    elif c1.get()==1 and c2.get()==1 and c3.get()==0:
        courseu = "Java/PHP"
    elif c1.get()==1 and c2.get()==0 and c3.get()==1:
        courseu = "Java/Python"
    elif c1.get()==1 and c2.get()==0 and c3.get()==0:
        courseu = "Java"
    elif c1.get()==0 and c2.get()==1 and c3.get()==1:
        courseu = "PHP/Python"
    elif c1.get()==0 and c2.get()==1 and c3.get()==0:
        courseu = "PHP"
    elif c1.get()==0 and c2.get()==0 and c3.get()==1:
        courseu = "Python"
    else:
        courseu = "NONE"

    print(courseu)

    sql.execute("SELECT email FROM loginDataTable")
    emailData=sql.fetchall()
    if emailu in emailData:
        print("this email already exixts")
    else:
        query = "INSERT INTO loginDataTable values" \
                "('%s','%s','%s','%s','%s','%s','%s')" \
                % (nameu, cityu, phoneNou, emailu, passwordu, genderu, courseu)
        sql.execute(query)
        connection.commit()
        print("data inserted successfully")




button=t.Button(root,text="submit",command=submitForm)
button.grid(column=1,row=7,pady=10)

root.mainloop()
