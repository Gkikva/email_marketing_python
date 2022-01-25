from send_html_to_client import *
from send_file_to_client import *

EMAIL_ADDRESS=""
EMAIL_PASS = ""
FILE_NAME = ""
MESSAGE_SUBJECT = ""
client_mail_list = ""


user_needs = input("what you want to send? HTML or file:  ")
if user_needs == "HTML" or user_needs == "html":
    HTML_sender(client_mail_list, MESSAGE_SUBJECT, EMAIL_ADDRESS, EMAIL_PASS)
if user_needs == "FILE" or user_needs == "file":
    FILE_sender(client_mail_list, MESSAGE_SUBJECT, EMAIL_ADDRESS, EMAIL_PASS, FILE_NAME)
