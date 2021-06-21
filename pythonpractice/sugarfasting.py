sugarlevel = int(input("Enter your sugar level"))
if sugarlevel>=80 and sugarlevel<=100:
    print("it is normal")
elif sugarlevel<80:
    print("sugar level low")
elif sugarlevel>100:
    print("sugar level is high")
