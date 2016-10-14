import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('bandit.labs.overthewire.org', username='bandit5', password='koReBOKuIDDepwhWk7jZC0RTdopnAYKh')
stdin, stdout, stderr = ssh.exec_command('find . -type f -size 1033c | xargs cat {}')
lines = stdout.readlines()
for line in lines:
        if line.strip():
		print line
