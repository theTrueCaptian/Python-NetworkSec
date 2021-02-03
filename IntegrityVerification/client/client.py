from socket import *
from Crypto.Cipher import AES
import sys
import select
import string
import thread
import socket
import select
import socket
import threading
import time
#from cryptography.fernet import Fernet
from Crypto.Cipher import AES
import hmac
import hashlib
from hashlib import sha1
from time import time
import re

IS_TCP = True
IS_CHECK_AUTH = True


HOST = '127.0.0.1'
PORT = 8080
ADDR = (HOST, PORT)


def chat_client():
	last_time_message = 0 

	#if(len(sys.argv) == 2) :
	#	print 'Usage : python chat_client.py hostname port'
	#	sys.exit()

	if IS_TCP:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(2)

		# connect to remote host
		try :
			s.connect(ADDR)
		except :
			print 'Unable to connect'
			sys.exit()
    
	else:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	 
	 
	print 'Connected to remote host. You can start sending messages'
	sys.stdout.write(''); sys.stdout.flush()
     
	while 1:
		socket_list = [sys.stdin, s]
		 
		# Get the list sockets which are readable
		ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
		 
		for sock in ready_to_read:             
			if sock == s:
				
				# incoming message from remote server, s
				if IS_TCP:
					data = sock.recv(4096)
				else:
					data, server = sock.recvfrom(4096)

				if not data :
					print '\nDisconnected from chat server'
					sys.exit()
				else :
					
					#Decrypt the message if the user has indicated password
					if data[0:7]!='Server>' and key!='' and IS_CHECK_AUTH:

						#Read in the hmac
						split = data.split(';hmac=')
						data = split[0]
						mac = split[1]

						#Verify the mac on the data
						expected_mac = hmac.new(key,data,hashlib.sha1)
						if not hmac.compare_digest(expected_mac.hexdigest(), mac):
							print "\nWarning! The following message has been tampered with OR you dont have the right key."

						# Decryption
						decryption_suite = AES.new(key, AES.MODE_CBC, 'This is an IV456')
						plain_text = decryption_suite.decrypt(data)
						
						#Verify no one has replayed this message, by checking the timestamp and the current time
						matchObj = re.match( r'\[([0-9]+)\.*[0-9]*\].*', plain_text)
						if matchObj:
							#if the last time a message was received is greater than this message timestamp, then the message was replayed
							if long(matchObj.group(1))<last_time_message :
								print "And the message was also replayed."
							else:
								last_time_message = long(matchObj.group(1))

						#print data
						sys.stdout.write('\n'+plain_text)

					else:
						#print data
						sys.stdout.write('\n'+data)
					
					sys.stdout.write('\n'); sys.stdout.flush()     


            
			else :
				# user entered a message
				msg = sys.stdin.readline()

				if key!='' and IS_CHECK_AUTH:
					whole_message = "["+str(time())+"]"+alias+">"+msg
					padding = (int)(float(16*(int)(len(whole_message)/16+1)))	# float(16*(int)(100/16+1)) = 112
					whole_message = whole_message.ljust(padding)
					
					#Encryption
					encryption_suite = AES.new(key, AES.MODE_CBC, 'This is an IV456')
					cipher_text = encryption_suite.encrypt(whole_message)
		
					digest_maker = hmac.new(key,cipher_text,hashlib.sha1)

					final_message = cipher_text+';hmac='+digest_maker.hexdigest()

					if IS_TCP:
						s.send(final_message)
					else:
						s.sendto(final_message, ADDR)
				else:

					#Do not encrypt if the user didn't specify anything for the password
					final_message = "["+str(time())+"]"+alias+">"+msg
					if IS_TCP:
						s.send(final_message)
					else:
						s.sendto(final_message, ADDR)

				sys.stdout.write('Me>'+msg); sys.stdout.flush() 


if __name__ == "__main__":

	alias = raw_input("\nName: ")

	#Prompt the key that will decode the messages
	key = raw_input("\nPassword: ")
	if key!='':
		padding = (int)(float(16*(int)(len(key)/16+1)))
		key = key.ljust(padding)

	
	sys.exit(chat_client())

