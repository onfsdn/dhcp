#!/bin/bash

echo "--" > dhcp_offer_dump.txt
sudo dhcpdump -i eth0 | grep --line-buffered -B 15 OFFER >> dhcp_offer_dump.txt &
python offer.py
