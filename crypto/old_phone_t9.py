#!/usr/bin/python3

def translate(string):
    #print(string.split())
    new_string = []
    for item in string.split():
        if item == "0":
            new_string.append(" ")
        elif item == "2":
            new_string.append("A")
        elif item == "22":
            new_string.append("B")
        elif item == "222":
            new_string.append("C")
        elif item == "3":
            new_string.append("D")
        elif item == "33":
            new_string.append("E")
        elif item == "333":
            new_string.append("F")
        elif item == "4":
            new_string.append("G")
        elif item == "44":
            new_string.append("H")
        elif item == "444":
            new_string.append("I")
        elif item == "5":
            new_string.append("J")
        elif item == "55":
            new_string.append("K")
        elif item == "555":
            new_string.append("L")
        elif item == "6":
            new_string.append("M")
        elif item == "66":
            new_string.append("N")
        elif item == "666":
            new_string.append("O")
        elif item == "7":
            new_string.append("P")
        elif item == "77":
            new_string.append("Q")
        elif item == "777":
            new_string.append("R")
        elif item == "7777":
            new_string.append("S")
        elif item == "8":
            new_string.append("T")
        elif item == "88":
            new_string.append("U")
        elif item == "888":
            new_string.append("V")
        elif item == "9":
            new_string.append("W")
        elif item == "99":
            new_string.append("X")
        elif item == "999":
            new_string.append("Y")
        elif item == "9999":
            new_string.append("Z")
        else:
            new_string.append(item)
    #print(new_string)
    new_list = "".join(new_string)
    print(new_list)

if __name__ == "__main__":
    translate(input())
