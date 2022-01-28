import requests
from bs4 import BeautifulSoup
import smtplib,ssl,getpass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
now=datetime.datetime.now()

content=''

def extract_news(url):
    print("Extracting IndianExpress Stories.....")
    info=''
    info+=('<b>IndianExpress Stories</b>\n'+'<br>')
    response=requests.get('https://indianexpress.com/section/cities/delhi/')
    soup=BeautifulSoup(response.content,'html.parser')
    headlines=soup.find_all('h3')

    for i in range(len(headlines)):
        info+=((str(i+1)+'::'+headlines[i].text+"\n"+'<br>'))

    return (info)

cnt=extract_news('https://indianexpress.com/section/cities/delhi/')  
content+=cnt
content+=('<br>-----<br>')
content+=('End of Message')      

smtp_server="smtp.gmail.com"
port=587

sender_email=""
receiver_email=""

message=MIMEMultipart()
message["Subject"]="News Headlines Emailer"+"Dated: "+str(now.day)
message["From"]=sender_email
message["To"]=receiver_email

message.attach(MIMEText(content,'html'))
password=getpass.getpass(prompt="Enter your password: ")

context=ssl.create_default_context()
# The below code is used to establish a secure connection with Gmail's SMTP server

server=smtplib.SMTP(smtp_server,port)
server.starttls(context=context) # secure connection
server.login(sender_email,password)
print("Successful\n")

server.sendmail(sender_email,receiver_email,message.as_string())

