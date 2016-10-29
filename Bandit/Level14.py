from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit13'
password = '8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL'
cmd = "ssh -o StrictHostKeyChecking=no -i sshkey.private bandit14@localhost cat /etc/bandit_pass/bandit14 | nc 127.0.0.1 30000 | sed -e 's/Correct!//' | sed '/^\s*$/d'"

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
data = ex.recvall()

occur = [m.start() for m in re.finditer('\n', data)]
data = data[occur[len(occur)-2]+1:]
print data
