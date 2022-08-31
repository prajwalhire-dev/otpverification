#importing required py lib
import os
import random
import math
import smtplib

#now we will generate a random num and store it in a variable
digit = '0123456789'
OTP = ''

#math. floor() function returns the largest integer not greater than input
#random.random() returns a random float in the range [0.0, 1.0)
#*10 to keep the otp in range of 0 to 9
for i in range(6):
    OTP += digit[math.floor(random.random()*10)]

otp = OTP + ' is your OTP'

message = otp

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

emailid = input('Enter your email:')
s.login('thedimensionscience@gmail.com', 'sabfwioraemnewqy')
s.sendmail('&&&&&&', emailid, message)

a = input('Enter your OTP :')
if a == OTP:
    print('verified')
else:
    print('Please check the OTP again')

