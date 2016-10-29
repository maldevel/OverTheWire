from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit1'
password = 'boJ9jbbUNNfktd78OOpsqOltutMc3MY1'
cmd = 'cat < -'

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

