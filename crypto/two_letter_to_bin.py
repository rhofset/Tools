#!/usr/bin/python3


def to_bin(input_string):
    new_string = []
    for item in list(input_string):
        if item == "r":
            new_string.append("1")
        elif item == ",":
            new_string.append("0")
    #print(new_string)
    new_list = "".join(new_string)
    print(new_list)
    #print(len(new_list))

if __name__ == "__main__":
    to_bin(input())