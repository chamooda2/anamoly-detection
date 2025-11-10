import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
def email_sender(recipient_email,message):
    smtp_port = 587
    smtp_server = "smtp.gmail.com"

    sender_email = "thecuatroteam@gmail.com"
  
    pswd = "qesxgeacakgplngp"

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


# secret = "Buffed2Gloves"

# def send_sms(sender_email, sender_password, recipient_number, message):
#     # Set up the SMTP server
#     smtp_server = 'smtp.gmail.com'
#     smtp_port = 587

#     # Format the recipient's email address based on the SMS gateway
#     sms_gateway = {
#         'AT&T': '@txt.att.net',
#         'Verizon': '@vtext.com',
#         'T-Mobile': '@tmomail.net',
#         # Add more gateways as needed
#     }

#     recipient_email = recipient_number + sms_gateway['AT&T']  # Replace 'AT&T' with the appropriate carrier

#     # Create the email message
#     email_message = f"From: {sender_email}\nTo: {recipient_email}\nSubject: SMS Message\n\n{message}"

#     try:
#         # Establish a secure connection with the SMTP server
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()
        
#         # Log in to the email account
#         server.login(sender_email, sender_password)
        
#         # Send the email message
#         server.sendmail(sender_email, recipient_email, email_message)
        
#         print('SMS sent successfully')
#     except Exception as e:
#         print(f'Error sending SMS: {e}')
#     finally:
#         # Close the connection to the SMTP server
#         server.quit()


# sender_email = 'asadhadi2222@gmail.com@gmail.com'
# sender_password = secret  # Replace with your email password
# recipient_number = '+91 9219414980'  # Replace with the recipient's phone number
# message = 'Will this work?'  # Replace with your desired message

# send_sms(sender_email, sender_password, recipient_number, message)
