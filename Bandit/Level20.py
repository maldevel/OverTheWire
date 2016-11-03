from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit20'
password = 'GbKksEFF4yrVs6il55v6gwY5aVje5f0j'
cmd1 = "cat /etc/bandit_pass/bandit20 | nc -l 2626 &"
cmd2 = './suconnect 2626'

s =  ssh(host=hostname, user=username, password=password)
sh = s.run('bash')
sh.recv(timeout=5).decode()
sh.sendline(cmd1)
sh.recv(timeout=5).decode()
sh.sendline(cmd2)
print sh.recv(timeout=10).decode().split('\n')[2]


