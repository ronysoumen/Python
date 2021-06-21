population={}
print(dir(population))
population={"China": 143,"India":136,"USA":32,"Pakistan":21}
print(population.keys())
User=input("WHAT DO YOU WANT TO DO")
if User.lower()=="print":
    for k,v in population.items():
        print(f"{k}===>{v}")
elif User.lower()=="add":
    countryname=input("What is the country you want to add")
    if population.__contains__(countryname):
        print("It exist and do nothing")
    else:
        populationo_newCountry=input("What is the population")
        population[countryname]=populationo_newCountry
        print(population)
elif User.lower()=="remove":
    countryname=input("What is the country you want to remove")
    if population.__contains__(countryname):
        population.__delitem__(countryname)
        print(population)
    else:
        print(f"No country such as {countryname} is there in the list , so can not be removed ")
elif User.lower()=="query":
    countryname=input("What is the country, you are willing to know about")
    if population.get(countryname):
        print(f"{countryname} has a population of {population[countryname]}")

    else:
        print(f" I am sorry no such{countryname} is there in the list ,try again")






