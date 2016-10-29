from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit3'
password = 'UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK'

s =  ssh(host=hostname, user=username, password=password)
cmd = s.run('cat inhere/.hidden')
print cmd.recvall()

