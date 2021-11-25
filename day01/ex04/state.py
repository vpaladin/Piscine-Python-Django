import sys

def get_key(val, dict):
    for x,y in dict.items():
        if y == val:
            return x
    return None

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
        if sys.argv[1] in capital_cities.values():
            print(get_key(get_key(sys.argv[1], capital_cities), states))
        else:
            print("Unknown capital city")