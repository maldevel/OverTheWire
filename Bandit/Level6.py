from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit5'
password = 'koReBOKuIDDepwhWk7jZC0RTdopnAYKh'
cmd = 'find . -type f -size 1033c | xargs cat {}'

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

