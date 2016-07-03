#!/usr/bin/bash
yaml_file="faucet.yaml"
IP=$1

cp faucet.yaml.bk $yaml_file
echo "acls:"  >> $yaml_file
echo "  1:" >> $yaml_file
echo "    - rule:" >> $yaml_file
echo "        ip_dst: $IP" >> $yaml_file
echo "        dl_type: 0x800" >> $yaml_file
echo "        allow: 1" >> $yaml_file
