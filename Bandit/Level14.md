###Bandit Level 14

####Solution
```
	ssh bandit13@bandit.labs.overthewire.org
	ssh -o StrictHostKeyChecking=no -i sshkey.private bandit14@localhost cat /etc/bandit_pass/bandit14 | nc 127.0.0.1 30000 | sed -e 's/Correct!//' | sed '/^\s*$/d'
```


#####Key for Level 15
```
	BfMYroe26WYalil77FoDi9qh59eK5xNr
```
