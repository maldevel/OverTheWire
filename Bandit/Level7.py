import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('bandit.labs.overthewire.org', username='bandit6', password='DXjZPULLxYr17uwoI01bNLQbtFemEgo7')
stdin, stdout, stderr = ssh.exec_command('find / -type f -user bandit7 -group bandit6 -size 33c 2> /dev/null | xargs cat')
lines = stdout.readlines()
for line in lines:
        if line.strip():
		print line
