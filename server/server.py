
import sqlite3 as sql
import socket
import threading

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
		
def client_thread(ct_sock, ct_addr):
	print "client thread started"
	ct_sock.send('ACK')
	
	# start a p2p connection for sending undelivered data
	print ct_sock.recv(1024)
	myClient = client(ct_addr[0], ct_addr[1]) 
	ct_sock.close()
	myClient.sock.send('hello')
	
def main():
	myServer = server(1235);
	db = sql.connect('chat_server.db')
	db_c = db.cursor()
	
	while 1:
		client, addr = myServer.sock.accept()
		print "connected to " + str(client)+ " with address " + str(addr)
		t = threading.Thread(target = client_thread, args = (client, addr,))
		t.start()
		
main()