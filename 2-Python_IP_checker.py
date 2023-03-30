def isValidIP(ip):
    isValid = True
    if ip.count(".") == 3:
        for octet in ip.split("."):
            if not ((0 <= int(octet) <= 255) and octet == str(int(octet))):
                isValid = False
    else:
        isValid = False

    return isValid


def ipConvertor(ip):
    binary = ""
    octal = ""
    hexa = ""
    for octet in ip.split("."):
        binary += (bin(int(octet))[2:].zfill(8))
        binary += "."

        octal += (oct(int(octet))[2:].zfill(4))
        octal += "."

        hexa += (hex(int(octet))[2:].zfill(2))
        hexa += "."

    lst = [ip, binary[:-1], octal[:-1], hexa[:-1]]
    return lst


iplist = []
for _ in range(10):
    ip = input("Enter ipv4 address : ").strip()
    if isValidIP(ip):
        lst = ipConvertor(ip)
        line = ",".join(lst) + '\n'
        iplist.append(line)

with open("conversion.txt", "w") as file:
    file.writelines(iplist)

with open("conversion.txt") as file:
    lines = file.readlines()
    print(*lines, sep="")