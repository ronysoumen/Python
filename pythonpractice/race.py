flag=0
for i in range(5):
    question = input("are you tired yes/no?")
    if question == 'yes':
        flag = 1
        break
    else:
        flag = 0
        continue
if flag == 1:
    print("you didn't finish the race")
else:
    print("congratulations you have finished")


