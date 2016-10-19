import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('bandit.labs.overthewire.org', username='bandit15', password='BfMYroe26WYalil77FoDi9qh59eK5xNr')
stdin, stdout, stderr = ssh.exec_command("echo 'BfMYroe26WYalil77FoDi9qh59eK5xNr' | openssl s_client -connect 127.0.0.1:30001 -quiet | sed -e 's/Correct!//' | sed '/^\s*$/d'")
lines = stdout.readlines()
for line in lines:
        if line.strip():
		print line
