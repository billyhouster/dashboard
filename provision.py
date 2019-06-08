
import paramiko

key = paramiko.RSAKey.from_private_key_file('./billy.pem')

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(hostname='18.224.73.90', username='ubuntu', pkey=key)

commands = [
        'sudo aptitude update -y',

        'mkdir app',
        'cd app',
        'git clone https://github.com/billyhouster/dashboard.git',

        'pip3 install -r dashboard/requirements.txt',
        'sudo python3 dashboard/app.py',

]

for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode(), stderr.read().decode())
