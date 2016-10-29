from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit0'
password = 'bandit0'
cmd = 'cat readme'

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

