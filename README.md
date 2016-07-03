# dhcp

# Start the capture program:

    ./start_monitor.sh

Above command will start the tcp dump and push al offer packet details to the dhcp_offer.txt file
Now another program offer.py wil run and it will keep on pull the offer packet info and parse it to get IP and mac
Once it gets the IP and mac it writes it to the yaml file as a rule to faucet

## Solution Notes - Integrate with Enterprise DHCP Server

-  Ramesh C
-  Naggappan Ramukannan
-  Raghavachari Mulugu

## IP Address Conflicts on a DHCP Network and DDoS Attacks


- On a non-SDN Network, when a client request an IP address,  the DHCP can return one, However, the client can actually use any address it wants. It can even use an IP address that conflicts with another host. This leads to  IP address conflicts on a DHCP Network. 
- Hackers can spoof the packet and make a network vulnerable to Distributed Denial of Service (DDoS) attacks


## Solution Approach



- Analyze the DHCP packets


- Create an ACL based on the DHCP packets


- From DHCP offer packets, create rules (allow) mapping an IP address with MAC addresses 


- Clear rules when there is a DHCP release
   

 
[Intergrate with Enterprise DHCP Server](https://github.com/geethabg/Images/blob/master/DHCP_ACL_Controller.png) 

  ![alt text](DHCP_ACL_Controller.png "Intergrate with Enterprise DHCP Server")

 

## Deployment

    git clone https://github.com/onfsdn/dhcp.git
    cd dhcp
    ./start_monitor.sh




