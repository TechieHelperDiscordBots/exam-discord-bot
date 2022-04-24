import sys

while True:
    d = []
    
    ip = input()
    if len(ip) == 1:
        continue

    ip = ip.split(" ")

    name = ""
    while True:
        try:
            int(ip[0][0])
            break
        except:
            name += ip[0] + " "
            ip.pop(0)
        
    d.append(name)

    d.append(ip[0])
    ip.pop(0)
    d.append(ip[-1])
    ip.pop(-1)

    date = ""
    date += ip[-1] + " "
    ip.pop(-1)
    date += ip[-1] + " "
    ip.pop(-1)
    date += ip[-1] + " "
    ip.pop(-1)
    d.append(date)

    ip.pop(-1)
    d.append(" ".join(ip))
    
    
    print("[\"" + d[3] + "\", \"" + d[1] + "\", \"" + d[0] + "\", \"" + d[4] + "\", \"" + d[2] + "\", \"0\"],")

                

        
