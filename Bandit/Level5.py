import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('bandit.labs.overthewire.org', username='bandit4', password='pIwrPrtPN36QITSp3EQaw936yaFoFgAB')
stdin, stdout, stderr = ssh.exec_command('cat < inhere/-file07')
lines = stdout.readlines()
for line in lines:
        print line
