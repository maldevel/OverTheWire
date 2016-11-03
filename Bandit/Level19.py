from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit19'
password = 'IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x'
cmd = './bandit20-do cat /etc/bandit_pass/bandit20'

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

