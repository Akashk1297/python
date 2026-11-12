import paramiko
import logging

client=paramiko.SSHClient()
logging.basicConfig(file='',level=logging.INFO)

count1=0
count2=0
file=''

with open(file) as f:
    for server in f:
        try:
            client.connect(hostname=server,username='',password='',key_filename='')
            client.load_host_keys()
            stdin,stdout,stderr=client.exec_command('df','-h')
            op1= stdout.read().decode()
            op2= stderr.read().decode()

            if op1.return_code !=0:
                raise RuntimeError

        except paramiko.AuthenticationException:
            logging.info('AuthenticationException')
            count1+=1
        except paramiko.SSHException:
            logging.info('SSHException')
            count2+=1
        finally:
            client.close()


