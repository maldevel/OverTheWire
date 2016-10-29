from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit11'
password = 'IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR'
cmd = "cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m' | sed -e 's/The password is //'"

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

