import smtplib

server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
a=input("enter mail")
b=input("enter password")
server.login('%s'%a,'%s'%b)



# server.sendmail('yashg1709@gmail.com',
#                 'nandkk07@gmail.com',
#                 "F**K OFF!!! ;)")

server.sendmail('yashg1709@gmail.com',
                'nandkk07@gmail.com',
                "___")

server.quit()

print("email sent successfully")