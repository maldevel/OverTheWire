from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit18'
password = 'kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd'
cmd = 'cat readme'

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

