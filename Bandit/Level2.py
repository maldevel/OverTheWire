from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit1'
password = 'boJ9jbbUNNfktd78OOpsqOltutMc3MY1'

s =  ssh(host=hostname, user=username, password=password)
cmd = s.run('cat < -')
print cmd.recvall()

