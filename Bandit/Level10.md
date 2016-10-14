###Bandit Level 10

####Solution
```
	ssh bandit9@bandit.labs.overthewire.org
	strings data.txt | grep '==' | awk -F' ' '{print $2}' | awk 'length($0)==32'
```


#####Key for Level 11
```
	truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```
