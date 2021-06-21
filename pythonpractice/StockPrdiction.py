import re
with open("g.csv","r") as f,open("output.csv","w") as out:
    out.write("Company Name,PE Ratio,PB Ratio\n")
    next(f)
    for line in f:
        #print(line)
        #s=tokens[0]
        tokens=line.split(",")


       # print(tokens)
        stock=tokens[0]
        price=float(tokens[1])
        earning=float(tokens[2])
        bookvalue=float(tokens[3])
        PE=price/earning
        PB=price/bookvalue

        out.write(f"{stock},{PE},{PB}\n")