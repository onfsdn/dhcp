#!/usr/bin/python
##########################################################################

#code to collect MAC and its IP address from dhcp sniffing file

###########################################################################

import time

def read_data():
    count = 0
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
               IP = line.split()[2][1:-1]
#               print IP
            if count == 10:
               mac = line.split()[1]
#               print mac
               print IP + " " + mac
            count += 1

read_data()
