import socket

class client():
	def __init__(self, host, port):
		self.sock = socket.socket()
		self.host = host 
		self.port = port
		self.sock.connect((host,port))

def main():
	myClient = client('127.0.0.1', 1235);
	print myClient.recv()

main()