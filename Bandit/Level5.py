from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit4'
password = 'pIwrPrtPN36QITSp3EQaw936yaFoFgAB'
cmd = 'cat < inhere/-file07'

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

