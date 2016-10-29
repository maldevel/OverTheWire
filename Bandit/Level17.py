from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit17'
password = 'xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn'
cmd = 'diff passwords.new passwords.old | grep \'<\' | sed -e "s/<\s//"'

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

