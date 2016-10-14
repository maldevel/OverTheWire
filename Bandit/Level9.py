import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('bandit.labs.overthewire.org', username='bandit8', password='cvX2JJa4CFALtqS87jk27qwqGhBM9plV')
stdin, stdout, stderr = ssh.exec_command('sort data.txt | uniq -u')
lines = stdout.readlines()
for line in lines:
        if line.strip():
		print line
