from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit9'
password = 'UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR'
cmd = "strings data.txt | grep '==' | awk -F' ' '{print $2}' | awk 'length($0)==32'"

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

