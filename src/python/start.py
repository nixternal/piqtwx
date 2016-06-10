#!/usr/bin/env python

import fcntl
import os
import socket
import struct
import subprocess
import sys
import time


def get_pid(name):
    p = subprocess.Popen(
        "ps aux | grep %s | grep -v grep | awk -F' ' '{print $2}'" % name,
        shell=True,
        stdout=subprocess.PIPE
    )
    o = p.communicate()[0].strip()
    return o


def get_ip(ifname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,
            struct.pack('256s', ifname[:15])
        )[20:24])
    except IOError:
        return None

if get_pid('piqtwx.py'):
    sys.exit(0)
ip = None
wlan0 = None
while not wlan0:
    ip = get_ip('wlan0')
    if ip:
        wlan0 = True
    time.sleep(1)
os.system('/usr/bin/python -B /home/pi/piqtwx/piqtwx.py')
