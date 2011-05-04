#!/usr/bin/env python2.7
#coding=utf-8
'''
Created on May 4, 2011

@author: dawn
'''
import urllib2
import logging
import time
import traceback as tb 
from urllib2 import URLError
import socket

l = logging.getLogger('dlmeter')

svrs =[
'04',
'27',
'14',
'25',
'05',
'09',
'06',
'10',
'13',
'23',
'24',
'11',
'17',
'22',
'19',
'16',
'21',
'07',
'32',
'15',
'31',
'33',
'34',
'08',
'26'      
]

TEST_SIZE = 1024*128

def calc(size,time):
    kilo = size/1024
    kps = kilo/time
    return kps

def make_list(tags):
    result = []
    for snum in tags:
        tag = str(snum)
        url = 'http://s'+tag+'.flyssh.com/10mb.bin'
        result.append(url)
    return result

def report(url,kps):    
    l.info('%s %d K/s',url,kps)
    
def download(url):
    try:
        f = urllib2.urlopen(url,timeout=1)
        st = time.time()
        f.read(TEST_SIZE)
        et = time.time()
        return et - st
    except URLError as e :
        l.info('%s open url error %r',url,e.reason)
    except socket.timeout as e:
        l.info('%s read time out ',url)
    else:
        l.warning('unhandled error %r',tb.format_exc())


def main():
    print 'starting ... '
    for url in make_list(svrs):
        elaps = download(url)
        if elaps is not None:
            kps = calc(TEST_SIZE,elaps)
            report(url,kps)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(message)s')
    l.level = logging.INFO
    main()