# from MAIL_SENDER import *
import csv
import smtplib
from email.message import EmailMessage
import time



def HTML_sender(client_mail_list ,MESSAGE_SUBJECT, EMAIL_ADDRESS, EMAIL_PASS ):
    sleep_counter = 0
    mail_was_sended = 0
    with open(client_mail_list) as f:
        user_input = input(str("have you checked everything on HTML sender?  yes / no "))
        reader = csv.DictReader(f)
        for row in reader:
            client = row['email']
            client_list = []
            client_list.append(client)
            for client_in_list in client_list:
                msg = EmailMessage()
                msg["subject"] = MESSAGE_SUBJECT #subject-ში რაც გინდა იმას მიუთითებ
                msg["from"] = EMAIL_ADDRESS
                msg["to"] = client_in_list
                #todo როდესაც გინდა გააგზავნო html template ფორმატი
                if user_input == "YES" or user_input == "yes":
                    with open("first_html.html", "r", encoding='utf-8') as f:
                        file_data = f.read()
                        file_n = f.name
                            #alternative-ის ახსნა არის დაახლოებით , ალტერნატიული ვარიანტი როგორ გავაგზავნოთო,
                            # msg.add_attachment ეს ბრძანება რომ ჩამწერეა, ის HTML გაიგზავნებოდა როგორც ფაილი
                        msg.add_alternative(file_data, subtype="html")
                else:
                    break

                try:
                    #todo რომ შეამოწმო თუ რატომ ერორდება, Try წაშალე და exept-მდე რაც წერია მიიტანე ბოლომდე მარცხნივ.
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.ehlo()
                    server.login(EMAIL_ADDRESS , EMAIL_PASS)
                    server.send_message(msg)
                    server.close()
                    print(f"Email was sent! on {client_in_list}  -- {sleep_counter}")
                    with open("working_mail.txt", "a" , encoding= 'utf-8') as working_mail:
                        working_mail.write(f"{client_in_list}\n")
                    sleep_counter += 1
                    mail_was_sended += 1

                except:
                    print (f'Something went wrong... on {client_in_list}  -- {sleep_counter}')
                    with open("bad_mail.txt", "a" , encoding= 'utf-8') as bad_mail:
                        bad_mail.write(f"{client_in_list}\n")
                    sleep_counter += 1

                if sleep_counter == 50:
                    print(f" now sleeping time !!! mail was sent to {mail_was_sended} client")
                    time.sleep(90)
                    sleep_counter = 0
                    print(sleep_counter)
