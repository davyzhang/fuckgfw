#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7
#coding=utf-8
'''
Created on Sep 14, 2011

@author: dawn
'''

import subprocess
import os
os.environ['PATH'] += ':/usr/local/bin/'

script_place = '' #script to start ssh_tunnel like '/Users/dawn/ssh_proxy.py'
process_token = '' #token used to determine the process by ps grep like '/usr/bin/ssh -f -N -g -D localhost:7070 .*flyssh.net'

shl='ps aux |grep "%(process_token)s"|grep -v "grep*"'%{'process_token':process_token}

try:
    out_put = subprocess.check_output(shl,shell=True)
    if out_put:
        print "proxy running skip this time..."
except:
    print "proxy is dead starting new one..."
    subprocess.call(script_place)
