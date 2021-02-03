from socket import *
import thread

import signal

IS_TCP = True

BUFF = 1024
HOST = '127.0.0.1'
PORT = 8080
MAX_CLIENTS = 10
CONNECTION_LIST = []

def close_handler(signum, frame):
	#This is called when the terminal session is closed
	serversocket.close()
	pass

#Safely close sockets when ctrl+c happens
# Otherwise this error would happen: http://stackoverflow.com/questions/19071512/socket-error-errno-48-address-already-in-use
#run> ps -fA | grep python
# kill <2nd num, proc num>
signal.signal( signal.SIGHUP, close_handler )

def broadcast_data (sock, message):
	#Do not send the message to master socket and the client who has send us the message
	for socket in CONNECTION_LIST:
		if socket != serversocket and socket != sock :
			try :
				socket.send(message)
			except :
				# broken socket connection may be, chat client pressed ctrl+c for example
				socket.close()
				CONNECTION_LIST.remove(socket)

#Call this when received
def client_handler(clientsocket, addr):
	#Send client information on the number
	clientsocket.send('Server>'+str(addr))
	print "Connected client from: "+str(addr)
	broadcast_data(clientsocket, "Server> Connected client from: "+str(addr))

	while 1:
		data = clientsocket.recv(1024)
		if not data:
			break
		print "Received Message: "+repr(data)
		broadcast_data(clientsocket, data)

	clientsocket.close()

ADDR = (HOST, PORT)
if IS_TCP:
	serversocket = socket(AF_INET, SOCK_STREAM)
	serversocket.bind(ADDR)
	serversocket.listen(MAX_CLIENTS) 
	# Add server socket to the list of readable connections
	CONNECTION_LIST.append(serversocket)
else:
	serversocket = socket(AF_INET, SOCK_DGRAM)
	serversocket.bind(ADDR)

print "Listening at "+str(HOST)+":"+str(PORT)

#Continuously listen for incoming clients and then pass the handler to client_handler()
while 1:
	if IS_TCP:
		clientsocket, addr = serversocket.accept()
		CONNECTION_LIST.append(clientsocket)
		thread.start_new_thread(client_handler, (clientsocket, addr))
		broadcast_data(clientsocket, "Server> [%s:%s] entered room\n" % addr)
	else:
		data, addr = serversocket.recvfrom(4096)
		if addr not in CONNECTION_LIST:
			CONNECTION_LIST.append(addr)
		print "Received Message from "+repr(addr)+": "+repr(data)+''
		#serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		#serversocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
		
		for address in CONNECTION_LIST:
			serversocket.sendto(data, address)


if IS_TCP:
	serversocket.close()