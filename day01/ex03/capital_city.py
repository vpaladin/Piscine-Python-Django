import sys

if __name__ == '__main__':
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    
    if len(sys.argv) == 2:
        temp = states.get(sys.argv[1])
        if temp != None:
            print(capital_cities.get(temp))
        else:
            print("Unknown state")