###Bandit Level 10

####Solution
```
	ssh bandit12@bandit.labs.overthewire.org
	mkdir /tmp/banditgame/ && cp data.txt /tmp/banditgame/ && cd /tmp/banditgame/ && 
	xxd -r data.txt data.gz && gzip -d data.gz && bzip2 -d -q data && mv data.out data.gz && 
	gzip -d data.gz && tar xf data && tar xf data5.bin && bzip2 -d -q data6.bin && 
	tar xf data6.bin.out && mv data8.bin data8.gz && gzip -d data8.gz && 
	cat data8 | sed -e 's/The password is //' && rm -rf /tmp/banditgame/ && cd ~
```


#####Key for Level 11
```
	8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```
