#!/usr/bin/env python3
from socket import gethostname, gethostbyname
from netifaces import AF_INET, AF_INET6, ifaddresses, interfaces, gateways
import sys
from pprint import pprint

if __name__ == '__main__':
  # Find host info
  host_name = gethostname()
  ip_address = gethostbyname(host_name)
  print("Host name: {0}".format(host_name))
  
  # Get interfaces list
  ifaces = interfaces()
  for iface in ifaces:
    if iface == sys.argv[1]:
      ipaddrs = ifaddresses(iface)
      if AF_INET in ipaddrs:
        ipaddr_desc = ipaddrs[AF_INET]
        ipaddr_desc = ipaddr_desc[0]
        print(f"Network interface: {iface}")
        print(f"\tIP address: {ipaddr_desc['addr']}")
        print(f"\tNetmask: {ipaddr_desc['netmask']}")
      if AF_INET6 in ipaddrs:
        pprint(ipaddrs[AF_INET6])

  # Find the gateway
  gateways = gateways()
  print(f"Default gateway: {gateways['default'][AF_INET][0]}")