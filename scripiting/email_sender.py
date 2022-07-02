import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'amirhossein hanifehzadeh'
email['to'] = 'hanifezadeham@outlook.com'
email['subject'] = 'you will be a good developer'

email.set_content("learning python!")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('amirhanife84@gmail.com', '09122377957')
    smtp.send_message(email)
    print('all good boss!')

