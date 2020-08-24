# Enumeration

## Information gathering:

### nmap - https://nmap.org/

Basic nmap scan:

```bash
nmap <IP>

nmap <HOST NAME>
```

To scan ranges:

```bash
nmap <IP/CIDR>

nmap <IP - extra last octet> example: nmap x.x.x.x - x

nmap <IP*> example: nmap x.x.x.* (scans x.x.x.1 to x.x.x.256)
```

Exclude ip from scan:

```bash
-- exlude
```

Nmap arguments:

```bash
-p      = port
-oN     = output as txt file
-oX     = output as xml file
-il     = read ips from file

```