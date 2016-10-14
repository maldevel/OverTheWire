import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('bandit.labs.overthewire.org', username='bandit1', password='boJ9jbbUNNfktd78OOpsqOltutMc3MY1')
stdin, stdout, stderr = ssh.exec_command('cat < -')
lines = stdout.readlines()
for line in lines:
        print line
