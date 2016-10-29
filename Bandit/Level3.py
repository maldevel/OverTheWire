from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit2'
password = 'CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9'

s =  ssh(host=hostname, user=username, password=password)
cmd = s.run('cat "spaces in this filename"')
print cmd.recvall()

