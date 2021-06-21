import statistics as stat
stocks={'INFOSYS':[600,630,620],
        'RELIANCE':[1420,1440,1450],
        'LNT':[200,230,230]}

def print_all():
    for keyval,values in stocks.items():
        print(f"{keyval}==>{values}==>{round(stat.mean(values),2)}")
def add_item():
    stockname=input("enter stock name")
    if stocks.get(stockname):
        print("can not be added, it is already there in the list")
    else:
        newstockame=input("enter the stockname you want to add")
        values=[]
        for i in range(3):
            values.append(int(input("enter value")))

        stocks[newstockame]=values
        print_all()
def amend_items():
    stockname = input("enter stock name")
    values = int(input("value you want to add"))
    if stockname in stocks:
        stocks[stockname].append(values)
    print(f"{values} is added in the stock {stockname} and see {print_all()}")

if __name__ == '__main__':
    amend_items()






