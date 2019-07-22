import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg=MIMEMultipart()    # create object of MIMEMultipart

msg['From'] = 'from_mail@gail.com'
msg['To'] = 'to_mail@gmail.com'
msg['Subject'] = "Subject of Mail"
filename = r"C:\Users\HP\Desktop\scc_notes.txt"

with open(filename, 'r') as f:
    message = MIMEText(f.read(),
                       _subtype="txt")
    message.add_header('Content-Disposition',
                       'attachment',
                       filename=filename) # attach file
    msg.attach(message)

body = "Your MEssage Here"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('from_mail@gmail.com','**********')

text = msg.as_string()
server.sendmail(msg['From'],msg['To'], text)
server.quit()

print("Email send Successfully")
