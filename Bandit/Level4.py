import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('bandit.labs.overthewire.org', username='bandit3', password='UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK')
stdin, stdout, stderr = ssh.exec_command('cat inhere/.hidden')
lines = stdout.readlines()
for line in lines:
        print line
