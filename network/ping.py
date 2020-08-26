#!/usr/bin/env python3

import argparse
import concurrent.futures
from datetime import datetime
import functools
from netaddr import IPNetwork
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
        not_ok_ip_addr.append(ip)

def hostaddr(ip):
    executor = concurrent.futures.ThreadPoolExecutor(254)
    ip_list = []
    for host in IPNetwork(ip):
        ip_list.append(host)
        f = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=254) as executor:
        for i in tqdm(ip_list):
            f.append([(host, executor.submit(functools.partial(ping, i)))])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-ip','--ipsubnet', help='IP address and subnet. Example: -IP <IP>/<SUBNET CIDR> or -IP <IP> for a single IP.',required=False)
    args = parser.parse_args()

    hostaddr(args.ipsubnet)
    print("\n")
    for i in sorted(ok_ip_addr):
        print(i)
    print("\n")
    print(datetime.now() - startTime)
    