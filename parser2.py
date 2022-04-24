import sys

data = []

input()
subjectName = "Bengali 8638"
while True:
    
    while True:
        d = []
        paper = input()
        spl = paper.split(" ")
        try:
            int(paper[0])
        except:
            subjectName = paper
            if paper == "OUT":
                print(data)
                for d in data:
                    print("[\"" + d[2] + "\", \"" + d[0] + "\", \"" + d[4] + "\", \"" + d[3] + "\", \"" + d[1] + "\", \"0\"],")
                sys.exit(0)
            break

        d.append(spl[0])
        spl.pop(0)

        d.append(spl[-1])
        spl.pop(-1)
        date = ""
        date += spl[-1] + " "
        spl.pop(-1)
        date += spl[-1] + " "
        spl.pop(-1)
        date += spl[-1] + " "
        spl.pop(-1)
        d.append(date)
        d.append(" ".join(spl))
        d.append(subjectName)

        data.append(d)

    
                

        
