import paramiko
import sys
import time
import yaml

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

def hello(name):
    print "Hello, %s!" % name
    config = yaml.safe_load(open("sshconfig.yml"))
    cmd_prompt = config["cmd_prompt"]
    
    c = paramiko.client.SSHClient()
    c.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)
    c.connect(config["sshsrv"], username=config["user"], password=config["passw"], look_for_keys=False)
    ch = c.invoke_shell()
    ch.set_combine_stderr(True)
    
    read_resp(ch, cmd_prompt)
    
    prompt = cmd_prompt
    
    resp = send_cmd(ch, name, prompt)
    time.sleep(1)
    c.close();

    return resp

def do_nothing():
    pass