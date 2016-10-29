from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit4'
password = 'pIwrPrtPN36QITSp3EQaw936yaFoFgAB'

s =  ssh(host=hostname, user=username, password=password)
cmd = s.run('cat < inhere/-file07')
print cmd.recvall()

