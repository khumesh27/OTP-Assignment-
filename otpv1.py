import random
import smtplib

otp = ''.join([str(random.randint(0,9))for i in range(6)])


server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('khumeshkhobragade32119@gmail.com','qzlxjfftbfieqwmu')
msg='HELLO YOUR OTP IS '+str(otp)
server.sendmail('khumeshkhobragade32119@gmail.com','khumeshkhobragade32119@gmail.com',msg)
server.quit()
