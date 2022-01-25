# email_marketing_python


python language is used


code is written to use in Email Marketing. you can send on client emails HTML templates, files, or just messages.
here is how you can use it. you have to have a Gmail account

to work code, you have to install those libraries
import csv
import smtplib
from email.message import EmailMessage
import time

you have to provide some information,  your Email with password, file_name = "what kind of file you want to send", MESSAGE_SUBJECT = "subject of emails "
client_mail_list = "the email list of client, it must be CSV file."


everything must be in the same folder where the code is. 

when you run code.  it will ask what you want to send, HTML template or file.   HTML template is provided on first_html.html, you have to paste HTML code in that template to be sended
