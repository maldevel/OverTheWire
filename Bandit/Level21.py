from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit21'
password = 'gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr'
cmd = 'cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv'

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

