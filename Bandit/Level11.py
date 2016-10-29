from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit10'
password = 'truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk'
cmd = 'base64 -d data.txt | sed -e "s/The password is //"'

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

