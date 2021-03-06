#!/usr/bin/env python3

"""
"/32" : "255.255.255.255",
"/31" : "255.255.255.254",
"/30" : "255.255.255.252",
"/29" : "255.255.255.248",
"/28" : "255.255.255.240",
"/27" : "255.255.255.224",
"/26" : "255.255.255.192",
"/25" : "255.255.255.128",
"/24" : "255.255.255.0",
"/23" : "255.255.254.0",
"/22" : "255.255.252.0",
"/21" : "255.255.248.0",
"/20" : "255.255.240.0",
"/19" : "255.255.224.0",
"/18" : "255.255.192.0",
"/17" : "255.255.128.0",
"/16" : "255.255.0.0",
"/15" : "255.254.0.0",
"/14" : "255.252.0.0",
"/13" : "255.248.0.0",
"/12" : "255.240.0.0",
"/11" : "255.224.0.0",
"/10" : "255.192.0.0",
"/9" : "255.128.0.0",
"/8" : "255.0.0.0",
"/7" : "254.0.0.0",
"/6" : "252.0.0.0",
"/5" : "248.0.0.0",
"/4" : "240.0.0.0",
"/3" : "224.0.0.0",
"/2" : "192.0.0.0",
"/1" : "128.0.0.0"
"""


def decimal_to_binary(subnet_mask):
    """
    Convert between subnet mask and CIDR
    """
    subnet_mask2 = subnet_mask.split(".")
    subnet_mask2 = list(map(int, subnet_mask2))
    subnet_mask3 = []
    for i in subnet_mask2:
        x = bin(i)
        y = str(x)
        subnet_mask3.append(y[2:])
    subnet_mask3 = "".join(subnet_mask3)
    #print(subnet_mask3, "test")
    return subnet_mask3


def subnet_mask_to_cidr(subnet_mask):
    subnet_mask = decimal_to_binary(subnet_mask)
    cdirsum = 0
    for i in subnet_mask:
        cdirsum += int(i)
        if i == 0:
            break
    return cdirsum


def cidr_to_subnet_mask(cidr):
    """
    Convert between CIDR and subnet mask
    """
    len_cidr = []
    for i in range(cidr):
        i = 1
        len_cidr.append(i)
    len_cidr2 = ",".join(str(i) for i in len_cidr)
    len_cidr3 = len_cidr2.replace(",", "")
    chars = 31
    for i in range(chars):
        if len(len_cidr3) <= 31:
            if i == "1":
                continue
            else:
                bit = str("0")
                len_cidr3 += bit
    len_cidr4 = [len_cidr3[0:8], len_cidr3[8:16], len_cidr3[16:24], len_cidr3[24:32]]
    len_cidr5 = []
    for i in len_cidr4:
        len_cidr5.append(int(i,2))
    return ".".join(map(str, len_cidr5))


def calc_broadcast_addr(addr = "192.168.0.1", mask = "255.255.255.0"):
    """
    Calculate the broadcast address.
    """
    #TODO Make a own function to add enough 0 in binary, maybe also add the b' so the '&' can work propertly. 
    addr = decimal_to_binary(addr)
    mask = decimal_to_binary(mask)
    print(addr, mask, "testing 1")
    binsum = int(addr) & int(mask)
    print(binsum, "testing 2")
    binsum = str(binsum)

    #Make this its own funct? Same as the 14 ish last lines in cidr_to_subnet_mask function...
    binsum2 = binsum.replace(",", "")
    chars = 31
    for i in range(chars):
        if len(binsum2) <= 31:
            if i == "1":
                continue
            else:
                bit = str("0")
                binsum2 += bit
    binsum_split = [binsum[0:8], binsum[8:16], binsum[16:24], binsum[24:32]]
    print(binsum_split, "testing 3")
    binsum_split2 = []
    for i in binsum_split:
        binsum_split2.append(int(i,2))
    return ".".join(map(str, binsum_split2))


def main():
    """
    Main menu
    """
    menu()
    input1 = input("What do you want to do? Anything else = exit\n")
    while input1:
        if input1 == "1":
            input2 = input("\nWhat is your subnet mask? Max 255.255.255.255\n")
            result2 = subnet_mask_to_cidr(input2)
            print("CIDR = {}{}\n".format("/", result2))
            main()
        elif input1 == "2":
            input3 = int(input("\nWhat is your CIDR?\n"))
            if input3 >32:
                print("\nTo hight number! Try again! Max is 32\n")
                input3 = int(input("\nWhat is your CIDR?\n"))
            result3 = cidr_to_subnet_mask(input3)
            print("{} is your network mask\n".format(result3))
            main()
        elif input1 == "3":
            input4 = input("\nWhat is your ip address?")
            input5 = input("\nWhat is your network mask?")
            result4 = calc_broadcast_addr(input4, input5)
            print("Your ip is: {}\n, and your network mask is: {}\n, then your broadcast address is: {}".format(input4, input5, result4))
        else:
            exit()


def menu():
    """
    Prints the menu
    """
    print("1. Convert from subnet mask to CIDR\n",
          "2. Convert from CIDR to subnet mask\n",
          "3. Find the broadcast address.\n")

if __name__ == "__main__":
    main()
