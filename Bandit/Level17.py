from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit17'
password = ''
cmd = ''

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

