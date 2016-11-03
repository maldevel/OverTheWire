###Bandit Level 10

####Solution
```bash
	ssh bandit9@bandit.labs.overthewire.org
	strings data.txt | grep '==' | awk -F' ' '{print $2}' | awk 'length($0)==32'
```
**Password**: *UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR*


#####Key for Level 11
```
	truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```
