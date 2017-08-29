'''
	threading
	networking
'''
import sqlite3 as sql

conn = sql.connect('chat.db')
c = conn.cursor()

def main():
	while(1):
			for id in check_unread():
				deliver(id)
			for id in check_unwritten():
				write(id)

def deliver(id):
	query = "select * from " + id 
	c.execute(query)
	return c.fetchall()

def write(id):
	pass 
	
def read(id):
	pass 