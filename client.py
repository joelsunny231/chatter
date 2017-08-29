'''
	MSG format:
		[#]tag:msg\n 
		tag -> recipient:sender 
'''
fin = open('server_joel.txt','r+')
fout = open('server_aswin.txt','r+')

userid = '@joel'
username = 'joel'


def main():
	read_msg()
	
def read_msg():
	fin.seek(0L,0)
	pos = fin.tell()
	for line in fin:
		pos_new = fin.tell()
		if line[0] != '#':
			[tag,msg] = extract(line)
			if tag[0] == userid:
				mark_read(pos)
				print tag[1] + ' : ' + msg 
				
		pos = pos_new 
			
def write_msg():
	fout.seek(0,2)
	input = ''
	while input != 'q':
		input = raw_input(" > ")
		if input != 'q':
			[recipient,msg] = input.split(" ",1)
			string = recipient+':'+username+':'+msg+'\n';
			fout.write(string)

def extract(line):
	recipient, sender, msg = line.split(':',2)
	return [[recipient,sender],msg]
	

def mark_read(pos):
	fout.seek(pos)
	fout.write('#')
		
main()