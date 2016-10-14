import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('bandit.labs.overthewire.org', username='bandit9', password='UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR')
stdin, stdout, stderr = ssh.exec_command("strings data.txt | grep '==' | awk -F' ' '{print $2}' | awk 'length($0)==32'")
lines = stdout.readlines()
for line in lines:
        if line.strip():
		print line
