
import sqlite3 as sql
import socket
import threading

class server():
	def __init__(self, port):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.host = socket.gethostname()
		self.port = port 
		self.sock.bind((host,port))
		self.sock.listen(5)

def client_thread(client):
	client.send('ACK')
	
def main():
	myServer = server(1235);
	db = sql.connect('chat_server.db')
	db_c = db.cursor()
	
	while 1:
		client, addr = myServer.sock.accept()
		threading.Thread(target = client_thread, args = (client,))
		
main()