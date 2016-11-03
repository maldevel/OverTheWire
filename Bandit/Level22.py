from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit22'
password = 'Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI'
cmd = 'cat /tmp/8ca319486bfbbc3663ea0fbe81326349'

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

