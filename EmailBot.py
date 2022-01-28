import smtplib,ssl,getpass

smtp_server="smtp.gmail.com"
port=587

sender_email=""
receiver_email=""

message="Hey there! This is an automated message"

password=getpass.getpass(prompt="Enter your password: ")

context=ssl.create_default_context()
# The below code is used to establish a secure connection with Gmail's SMTP server

server=smtplib.SMTP(smtp_server,port)
server.starttls(context=context) # secure connection
server.login(sender_email,password)
print("Successful\n")
# email context

server.sendmail(sender_email,receiver_email,message)

