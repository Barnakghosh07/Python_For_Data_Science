India= ["Mumbai", "Bengalore", "Chennai", "Delhi"]
usa = ["New York","Chicago","Las Vegas", "San Francisco"]
uk = ["London", "Manchester", "Liverpool", "Nottingham"]

# city = input("enter the city: ")
# if city in India:
#     print(f"{city} is in India")
# elif city in usa:
#     print(f"{city} is in USA")
# elif city in uk:
#     print(f"{city} is in UK")
# else: 
#     print("I don't know")

city1 = input("enter the city1: ")
city2 = input("enter the city2: ")

if city1 in India and city2 in India:
    print(f"{city1} and {city2} are in India")
elif city1 in usa and city2 in usa:
    print(f"{city1} and {city2} are in USA")
elif city1 in uk and city2 in uk:
    print(f"{city1} and {city2} are in UK")
else:
    print("They don't beleng to the same country")