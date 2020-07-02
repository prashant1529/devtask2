from smtplib import SMTP
sender_email = "awesomeprince1530@gmail.com"
receiver_email = "awesomeprince1530@gmail.com"
password = "eL0nMu$K15"
message = "Your code is not correct"
server = smtplib.SMTP('smtp.gmail.com',465)
server.starttls()
server.login(sender_email,password)
print('login successfully')

server.sendmail(sender_email,receiver_email , meassge)
print("Email has been sent to " ,receiver_email)
server.quit()
