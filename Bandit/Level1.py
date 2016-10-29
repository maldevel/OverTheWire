from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit0'
password = 'bandit0'

s =  ssh(host=hostname, user=username, password=password)
cmd = s.run('cat readme')
print cmd.recvall()

