import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('bandit.labs.overthewire.org', username='bandit11', password='IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR')
stdin, stdout, stderr = ssh.exec_command("cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m' | sed -e 's/The password is //'")
lines = stdout.readlines()
for line in lines:
        if line.strip():
		print line
