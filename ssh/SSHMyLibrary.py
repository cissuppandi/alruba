import paramiko
import sys
import time

def read_resp(ch, prompt):
    data = ""
    ch.timeout = 10

    while (prompt not in data):
        tmp = ch.recv(500)
        data += tmp
 
    return data

def send_cmd(ch, cmd, prompt):
    i = 0
    while( i < len(cmd) ):
        ch.sendall(cmd[i])
        i = i + 1

    ch.sendall("\x0d")
 
    return read_resp(ch, prompt)

def run_ssh_command(myCommand, myHost, myUser, myPasswd, myPrompt):
    
    c = paramiko.client.SSHClient()
    c.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)
    c.connect(myHost, username=myUser, password=myPasswd, look_for_keys=False)
    ch = c.invoke_shell()
    ch.set_combine_stderr(True)
    
    read_resp(ch, myPrompt)
    
    resp = send_cmd(ch, myCommand, myPrompt)
    time.sleep(1)
    c.close();

    return resp
run_ssh_command('sys','192.168.1.28','admin','1234567!','')
