#!/usr/bin/env python3


def divtest():
     subnet = {"/32" : "255.255.255.255",
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
              "/1" : "128.0.0.0"}


def subnet_mask_to_cidr(subnet_mask):
    """
    Convert between subnet mask and CIDR
    """
    subnet_mask2 = subnet_mask.split(".")
    subnet_mask2 = list(map(int, subnet_mask2))
    #print(subnet_mask2)
    subnet_mask3 = []
    for i in subnet_mask2:
        x = bin(i)
        y = str(x)
        subnet_mask3.append(y[2:])
    subnet_mask3 = "".join(subnet_mask3)
    cdirsum = 0
    for i in subnet_mask3:
        cdirsum += int(i)
        if i == 0:
            break
    return cdirsum


def cidr_to_subnet_mask(cidr):
    cidr2 = bin(cidr)
    len_cidr = []
    for i in range(cidr):
        i = 1
        len_cidr.append(i)
    #print(len_cidr)
    #print(len(len_cidr))
    len_cidr2 = ",".join(str(i) for i in len_cidr)
    #print(len_cidr2)
    #print(len(len_cidr2))
    len_cidr3 = len_cidr2.replace(",", "")
    #print(len_cidr3)
    #print(len(len_cidr3))
    chars = 31
    for i in range(chars):
        if len(len_cidr3) <= 31:
            if i == "1":
                continue
            else:
                bit = str("0")
                len_cidr3 += bit
    #print(len_cidr3)
    #print(len(len_cidr3))
    len_cidr4 = [len_cidr3[0:8], len_cidr3[8:16], len_cidr3[16:24], len_cidr3[24:32]]
    #print(len_cidr4)
    len_cidr5 = []
    for i in len_cidr4:
        len_cidr5.append(int(i,2))
    #print(len_cidr5)
    #len_cidr6 = ".".join(map(str, len_cidr5))
    #print(len_cidr6)
    return ".".join(map(str, len_cidr5))


def main():
    """
    Main menu
    """
    menu()
    input1 = input("What do you want to do? Anything else = exit\n")
    while input1:
        if input1 == "1":
            input2 = input("\nWhat is your subnet mask?\n")
            result2 = subnet_mask_to_cidr(input2)
            print("CIDR = {}{}".format("/", result2))
            main()
        elif input1 == "2":
            input3 = int(input("\nWhat is your CIDR?\n"))
            result3 = cidr_to_subnet_mask(input3)
            print("{}".format(result3))
        else:
            exit()


def menu():
    print("1. Convert from subnet mask to CIDR\n",
          "2. Convert from CIDR to subnet mask\n")

if __name__ == "__main__":
    main()
