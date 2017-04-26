### Bandit Level 16

#### Solution
```bash
	ssh bandit16@bandit.labs.overthewire.org
	nmap -sV -v -p31000-32000 127.0.0.1
	cat /etc/bandit_pass/bandit16 | openssl s_client -connect 127.0.0.1:31790 -quiet | sed -e 's/Correct!//' | sed '/^\s*$/d' > /tmp/bandit17.sshkey.private && chmod 400 /tmp/bandit17.sshkey.private && ssh -q -o StrictHostKeyChecking=no -i /tmp/bandit17.sshkey.private bandit17@localhost cat /etc/bandit_pass/bandit17 && rm -f /tmp/bandit17.sshkey.private
```
**Password**: *cluFn7wTiGryunymYOu4RcffSxQluehd*


##### Key for Level 17
```
	xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn

```
