import smtplib

server=smtplib.SMTP_SSL("smtp.gmail.com",465)
list_emial=["mehuljaiswal2012@gmail.com","kushagraagra008@gmail.com",]

server.login("kushagraagra008@gmail.com","25march2020l")
server.sendmail("kushagraagra008@gmail.com",list_emial,"Hey Naresh, This email is generated using python")

server.quit()