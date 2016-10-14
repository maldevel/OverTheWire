import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('bandit.labs.overthewire.org', username='bandit7', password='HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs')
stdin, stdout, stderr = ssh.exec_command("grep \"millionth\" data.txt | awk -F'\t' '{print $2}'")
lines = stdout.readlines()
for line in lines:
        if line.strip():
		print line
