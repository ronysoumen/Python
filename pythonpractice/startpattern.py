row = int(input("enter rows"))
col = int(input("enter columns"))
for i in range(row):
 s=''
 for j in range(col):
        #s = ''
        if j<=i:
         s=s + "*"
         print(s)
 print("\n")
