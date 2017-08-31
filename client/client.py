import socket

class server():
	def __init__(self, port):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.host = '127.0.0.1'
		self.port = port 
		self.sock.bind((self.host,self.port))
		self.sock.listen(5)

class client():
	def __init__(self, host, port):
		self.sock = socket.socket()
		self.host = host 
		self.port = port
		self.sock.connect((host,port))

def main():
	myClient = client('127.0.0.1', 1235);
	addr =  myClient.sock.getsockname()
	if myClient.sock.recv(1024) == 'ACK':
		myServer = server(addr[1])
		myClient.sock.send('OK')
		ct_sock , ct_ad = myServer.sock.accept()
		print "connected to " + str(ct_sock)+ " with address " + str(ct_ad)
		print ct_sock.recv(1024)

main()