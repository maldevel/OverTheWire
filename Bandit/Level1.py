import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('bandit.labs.overthewire.org', username='bandit0', password='bandit0')
stdin, stdout, stderr = ssh.exec_command('cat readme')
lines = stdout.readlines()
for line in lines:
        print line
