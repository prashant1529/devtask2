import smtplib
sender_email = "youremailaddress@gmail.com"
receiver_email = "youremailaddress@gmail.com"
password = "password"
message = "Your code is not working correctly"
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
print('login successfully')

server.sendmail(sender_email,receiver_email,message)
print("Email has been sent to ",receiver_email)
server.quit()
