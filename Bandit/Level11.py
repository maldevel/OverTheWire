import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('bandit.labs.overthewire.org', username='bandit10', password='truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk')
stdin, stdout, stderr = ssh.exec_command('base64 -d data.txt | sed -e "s/The password is //"')
lines = stdout.readlines()
for line in lines:
        if line.strip():
		print line
