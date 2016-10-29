from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit3'
password = 'UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK'
cmd = 'cat inhere/.hidden'

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

