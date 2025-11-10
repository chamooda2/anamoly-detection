import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
# def email_sender(email_to,message,img_path):
#     smtp_port = 587
#     smtp_server = "smtp.gmail.com"

#     email_from = "thecuatroteam@gmail.com"
#     pswd = "qesxgeacakgplngp"
    

   #email_context = ssl.create_default_context()
def email_sender(recipient_email,message):
    smtp_port = 587
    smtp_server = "smtp.gmail.com"

    sender_email = "sahilujwalagrawal@gmail.com"
  
    pswd = "vdwisymkqouqsuke"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "We need ---- help"

    msg.attach(MIMEText(message,'plain'))

    f = open("frame_1.jpg",'rb')
    img_data = f.read()

    img_mime = MIMEImage(img_data, name = os.path.basename("frame_1.jpg"))
    msg.attach(img_mime)


    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to the email account
        server.login(sender_email, pswd)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        print('Email sent successfully')


    except Exception as e:
        print(e)
    finally:
        server.quit()





def Police(path = "",Location = None):
    email_to = "asadhadi2020@gmail.com"
    email_sender(email_to,"We need Police here")
    if Location:
        print(Location)




def Ambulance(path = "",Location = None):
    email_to = "asadhadi2222@gmail.com"
    email_sender(email_to, "We need an Ambulance here")
    if Location:
        print(Location)


def FireTruck(path = "",Location= None):
    email_to = "sahilsunilagrawal@gmail.com"
    email_sender(email_to,"There is a Fire Outbreak over here")
    if Location:
        print(Location)




