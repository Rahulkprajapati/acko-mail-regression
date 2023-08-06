#!/usr/bin/env python
# coding: utf-8

# In[9]:


import smtplib
from email.message import EmailMessage

sender_mail="sender@gmail.com"
rec_mail="recei@gmail.com"
password="*********"
msg = ("XXXXXXXXXXXXXXXXXXX")

msg['Subject'] = 'Model trained'
msg['From'] = sender_mail
msg['To'] = rec_mail

# Send the message via our own SMTP server.
server = smtplib.SMTP_SSL('smtp.gmail.com', 587)
server.login(sender_mail,password)
print("Login Success")
server.send_message(msg)
print("Email has been sent to ",rec_mail)
server.quit()


# In[ ]:
