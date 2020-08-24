#!/usr/bin/env python3

import subprocess
import platform
import socket
from tqdm import tqdm
import concurrent.futures
import functools
from datetime import datetime


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
    

def hostaddr():
    executor = concurrent.futures.ThreadPoolExecutor(254)
    interface = socket.gethostbyname(socket.gethostname()).split(".")

    interface = interface[:-1]

    interface_joined = ".".join(interface)

    ip_list = []
    for i in range(255):
        host = interface_joined + "." + str(i)
        ip_list.append(host)
        f = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=254) as executor:
        for i in tqdm(ip_list):
            f.append([(host, executor.submit(functools.partial(ping, i)))])

    for i in ok_ip_addr:
        print(i)

    print("\n")
    print(datetime.now() - startTime)

if __name__ == "__main__":
    hostaddr()
