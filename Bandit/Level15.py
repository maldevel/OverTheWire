from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit15'
password = 'BfMYroe26WYalil77FoDi9qh59eK5xNr'
cmd = "echo 'BfMYroe26WYalil77FoDi9qh59eK5xNr' | openssl s_client -connect 127.0.0.1:30001 -quiet | sed -e 's/Correct!//' | sed '/^\s*$/d'"

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
data = ex.recvall()

occur = [m.start() for m in re.finditer('\n', data)]
data = data[occur[len(occur)-2]+1:]
print data

