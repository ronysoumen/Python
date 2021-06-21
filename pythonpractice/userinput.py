india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city = input("Enter the city name: ")
if city in india:
    print(f"{city} belongs to India")

elif city in pakistan:
    print(f"{city} belongs to pakistan")
else:
    print(f"{city} belongs to Bangladesh")

city1=input("enter city 1")
city2=input("enter city 2")
if city1 in india and city2 in india:
    print(" both of the cities are in india")
elif city1 in pakistan and city2 in pakistan:
    print(" both of the cities are in Pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print(" both of the cities are in bangladesh")
else:
    print(" both of the cities are not in same country")
