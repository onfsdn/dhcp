# dhcp

# Start the capture program:

    ./start_monitor.sh

Above command will start the tcp dump and push al offer packet details to the dhcp_offer.txt file
Now another program offer.py wil run and it will keep on pull the offer packet info and parse it to get IP and mac
Once it gets the IP and mac it writes it to the yaml file as a rule to faucet
