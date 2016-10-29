from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit8'
password = 'cvX2JJa4CFALtqS87jk27qwqGhBM9plV'
cmd = 'sort data.txt | uniq -u'

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

