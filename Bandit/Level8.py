from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit7'
password = 'HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs'
cmd = "grep \"millionth\" data.txt | awk -F'\t' '{print $2}'"

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

