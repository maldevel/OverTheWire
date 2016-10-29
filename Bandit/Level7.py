from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit6'
password = 'DXjZPULLxYr17uwoI01bNLQbtFemEgo7'
cmd = 'find / -type f -user bandit7 -group bandit6 -size 33c 2> /dev/null | xargs cat'

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

