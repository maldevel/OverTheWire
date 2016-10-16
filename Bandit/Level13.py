import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('bandit.labs.overthewire.org', username='bandit12', password='5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu')
stdin, stdout, stderr = ssh.exec_command("mkdir /tmp/banditgame/ && cp data.txt /tmp/banditgame/ && cd /tmp/banditgame/ && \
xxd -r data.txt data.gz && gzip -d data.gz && bzip2 -d -q data && mv data.out data.gz && \
gzip -d data.gz && tar xf data && tar xf data5.bin && bzip2 -d -q data6.bin && \
tar xf data6.bin.out && mv data8.bin data8.gz && gzip -d data8.gz && \
cat data8 | sed -e 's/The password is //' && rm -rf /tmp/banditgame/")
lines = stdout.readlines()
for line in lines:
        if line.strip():
		print line
