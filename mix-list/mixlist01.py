#!/usr/bin/env python3
my_list = [ "192.168.0.5", 5060, "UP" ]
print("The first item in the list (IP): " + my_list[0] )
print("The second items in the list (Port): " + str(my_list[1]) )
print("The last item in the list (State): " + my_list[-1] )
iplist = [ 5060, "80", 55,  "10.0.0.1", "10.20.30.1", "ssh" ]
print("IP Address: " + iplist[3],"and ", iplist[4])
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")

