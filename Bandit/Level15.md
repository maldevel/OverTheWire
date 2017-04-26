### Bandit Level 15

#### Solution
```bash
	ssh bandit15@bandit.labs.overthewire.org
	echo 'BfMYroe26WYalil77FoDi9qh59eK5xNr' | openssl s_client -connect 127.0.0.1:30001 -quiet | sed -e 's/Correct!//' | sed '/^\s*$/d'
```
**Password**: *BfMYroe26WYalil77FoDi9qh59eK5xNr*


##### Key for Level 16
```
	cluFn7wTiGryunymYOu4RcffSxQluehd
```
