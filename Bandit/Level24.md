### Bandit Level 24

#### Solution
```bash
	ssh bandit24@bandit.labs.overthewire.org

	for x in 56{6..7}{0..9}; do
	  echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $x | nc 127.0.0.1 30002 | egrep -v  "Exiting|Wrong|I am|Correct!" | sed "s/The password of user bandit25 is //";
	  echo "Try $x"; 
	done

```
**Password**: *UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ*


##### Key for Level 25
```
	uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
```
