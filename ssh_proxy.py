#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7
#coding=utf-8
'''
Created on Sep 14, 2011

@author: dawn
'''
import pexpect
import time
from subprocess import call

server = 's05.flyssh.net'

bind_ip = 'localhost'
bind_port = 7070
user_name = 'ssh_account'
password = 'ssh_password'

shl = 'ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no\
 -p %(port)d -f -N -g -D %(bind_ip)s:%(bind_port)s %(user_name)s@%(server)s'%{'bind_ip':bind_ip,
                                                                            'bind_port':bind_port,
                                                                            'server':server,
                                                                            'user_name':user_name,
                                                                            'port':port}token = '%(user_name)s@%(server)s'%{'user_name':user_name,'server':server}


def start_tunnel(shl,password):
    try:
        ssh_tunnel = pexpect.spawn(shl)
        print 'shl run ',shl
        index = ssh_tunnel.expect(['yes/no','password:'])
        if index == 0:
            print 'ensure connection'
            ssh_tunnel.sendline('yes')
            index = ssh_tunnel.expect(['password:'])
            print 'password asking...'
            time.sleep(0.1)
            ssh_tunnel.sendline(password)
        else:
            print 'password asking...'
            time.sleep(0.1)
            ssh_tunnel.sendline(password)
            print 'password sent waiting for done'
        time.sleep(5)
        ssh_tunnel.expect(pexpect.EOF)
        print 'done'
    except Exception,e:
        print str(e)

def end_tunnel():
    call('pkill -f %s'%token,shell=True)


if __name__ == '__main__':
    end_tunnel()
    start_tunnel(shl,password)
