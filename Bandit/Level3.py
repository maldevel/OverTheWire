import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('bandit.labs.overthewire.org', username='bandit2', password='CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9')
stdin, stdout, stderr = ssh.exec_command('cat "spaces in this filename"')
lines = stdout.readlines()
for line in lines:
        print line
