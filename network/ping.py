#!/usr/bin/env python3

import argparse
import concurrent.futures
from datetime import datetime
import functools
from netaddr import IPNetwork
import socket
import subprocess
import platform
from tqdm import tqdm

startTime = datetime.now()
ok_ip_addr = []
not_ok_ip_addr = []

def ping(ip):
    argument = '-n' if platform.system().lower() == 'windows' else '-c'
    ping_result = subprocess.getoutput("ping " + argument + " 1 " + str(ip))
    if "TTL" in ping_result:
        ok_ip_addr.append(ip)
    else: 
        not_ok_ip_addr.append(ip) # This is not in use at this moment

def host(ip):
    not_found = ['Hostname not found']
    try:
        host_name = socket.gethostbyaddr(str(ip))
        return host_name
    except:
        host_name = list(not_found)
        return host_name

def hostaddr(ip):
    ip_list = []
    for host in IPNetwork(ip):
        ip_list.append(host)
        f = []
    with concurrent.futures.ThreadPoolExecutor(254) as executor: # Change the number to how many threads you want.
        for i in ip_list:
            f.append([(host, executor.submit(functools.partial(ping, i)))])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-ip','--ipsubnet', help='IP address and subnet. Example: -IP <IP>/<SUBNET CIDR> or -IP <IP> for a single IP.',required=False)
    args = parser.parse_args()

    hostaddr(args.ipsubnet)
    print("\n")
    sorted_list = sorted(ok_ip_addr)
    sorted_list_host = []
    for i in tqdm(sorted_list):
        sorted_list_host.append(f"{i}, {host(i)[0]}")
    print("\n")
    for i in sorted_list_host:
        print(i)
    print("\n")
    print(datetime.now() - startTime)
