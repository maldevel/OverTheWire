from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit2'
password = 'CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9'
cmd = 'cat "spaces in this filename"'

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

