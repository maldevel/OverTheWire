import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('bandit.labs.overthewire.org', username='bandit13', password='8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL')
stdin, stdout, stderr = ssh.exec_command('ssh -o StrictHostKeyChecking=no -i sshkey.private bandit14@localhost cat /etc/bandit_pass/bandit14')
lines = stdout.readlines()
for line in lines:
        if line.strip():
		print line
