""" Julius Pazitka - Network scanner
https://www.geeksforgeeks.org/network-scanner-in-python/
https://www.thepythoncode.com/article/building-network-scanner-using-scapy

"""
import socket # This module provides socket operations and some related functions. Also support IP protocol.
from datetime import datetime # This module concrete date/time and related types for time measurement


network = input("Please, enter the IP address: ") 
network1 = network.split('.')
a = '.'

network2 = network1[0] + a + network1[1] + a + network1[2] + a # lists for each IP address (Start, end and enter IP address)
start_Number = int(input("Enter the Starting Number: "))
end_Number = int(input("Enter the Last Number: "))
end_Number = end_Number + 1
time1 = datetime.now() 

# It selects the range of IP address to ping sweep scan by splitting it into parts. This is followed by using
# a function for scanning the address, which further uses the socket.

def scan(addr):
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socket.setdefaulttimeout(1)
   result = s.connect_ex((addr,135))
   if result == 0:
      return 1
   else :
      return 0

# It gives the response about the host and time taken for completing the scanning process.

def run():
   for ip in range(start_Number,end_Number): 
      addr = network2 + str(ip)
      if (scan(addr)):
         print (addr , "is live")
         
run()
time2 = datetime.now()
total = time2 - time1
print("Scanning completed in:" , total, "seconds")
input("Please press any key")