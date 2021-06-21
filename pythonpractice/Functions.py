def fun_area(type="triangle",base=1 ,height=1,):
    if type=="triangle":
        return 1 / 2 * (base * height)
    else:
        return (base * height)



print(fun_area(input("enter type of shape").lower(),int(input("enter base")),int(input("enter height"))))
