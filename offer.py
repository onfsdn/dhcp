#!/usr/bin/python
##########################################################################

#code to collect MAC and its IP address from dhcp sniffing file

###########################################################################

import time
import os

def read_data():
    count = 0
    IP = ""
    mac = ""
    flag = "STOP"
    file = open("dhcp_offer_dump.txt",'r')
    while 1:
        where = file.tell()
        line = file.readline()
        if not line:
            time.sleep(1)
            file.seek(where)
        else:
            if "--" in line:
                count = 0
            if count == 1:
                mac = line.split()[5][1:-1]
            if count == 10:
                IP = line.split()[1]
                cmd = "./set_conf.sh " + IP
                if "ff:ff:ff:ff:ff:ff" in mac:
                    pass
                else:
                    os.system(cmd)
                    print IP + " " + mac
        count += 1

read_data()
