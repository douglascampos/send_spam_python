#!/usr/local/bin/python2.7

# Import smtplib for the actual sending function
import smtplib

from_addr = 'bruno.batalha@locaweb.com.br'
qtde 		 = 500
to_addrs  = 'suporte@lw.pleskw0016.hospedagemdesites.ws'

msg = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'

# Credentials (if needed)
username = 'bbatalha3'
password = 'kfix0064'

# The actual mail send
server = smtplib.SMTP('smtplw.com.br:587')
server.starttls()
server.login(username,password)

# Loop to send each email
for x in range(1, qtde):
	sub = "Test email spam number %i" % x
	message = 'Subject: %s\n\n%s' % (sub, msg)
	print "Sented mail numer => %i" % x
	server.sendmail(from_addr, to_addrs, message)

server.quit()
