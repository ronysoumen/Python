expense = int(input("enter the expense"))
expense_list = [2340, 2500, 2100, 3100, 2980]
flag=0
month=0
for ex in expense_list:
    if(ex==expense):
        flag=1
        month=expense_list.index(ex)
        break
if flag==1:
    print(f"month is {month}")
else:
    print("not included")

