import random
import smtplib
import re

def generate_OTP():
    global otp
    otp= ''.join([str(random.randint(0, 9)) for i in range(6)])

def send_otp():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('khumeshkhobragade32119@gmail.com', 'qzlxjfftbfieqwmu')
    msg = 'Dear Aspirant'+('Your Otp for login is /n') + str(otp)
    server.sendmail('khumeshkhobragade32119@gmail.com', s, msg)
    server.quit()

def validiate_email(s):

  pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
  if re.match(pat, s):
        print('valid email')
  else:
        print('Invalid email Format, Please enter valid email address!!')

global s
s= input('Enter your email address\n')



print(generate_OTP())
print(validiate_email(s))
send_otp()
