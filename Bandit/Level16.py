from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit16'
password = 'cluFn7wTiGryunymYOu4RcffSxQluehd'
cmd = "cat /etc/bandit_pass/bandit16 | openssl s_client -connect 127.0.0.1:31790 -quiet | sed -e 's/Correct!//' | sed '/^\s*$/d'"

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

