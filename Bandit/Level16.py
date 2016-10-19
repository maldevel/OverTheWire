import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('bandit.labs.overthewire.org', username='bandit16', password='cluFn7wTiGryunymYOu4RcffSxQluehd')
stdin, stdout, stderr = ssh.exec_command("cat /etc/bandit_pass/bandit16 | openssl s_client -connect 127.0.0.1:31790 -quiet | sed -e 's/Correct!//' | sed '/^\s*$/d'")
lines = stdout.readlines()
key = ''
for line in lines:
        if line.strip():
		key = key + line
print key
