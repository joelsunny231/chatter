import sqlite3 as sql 

conn = sql.connect('chat_server.db')

c = conn.cursor()

c.execute(''' create table users(id integer primary key, uname text, status integer, undelivered integer, connection text)''')

c.execute("insert into users values(1,'joel',1,0,null)")
c.execute("insert into users values(2,'aswin',1,0,null)")

c.execute(''' create table t1(msg text) ''')
c.execute(''' create table t2(msg text) ''')

conn.commit()
