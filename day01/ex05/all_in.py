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
        arg = (sys.argv[1].split(','))
        arg = [x.strip().title() for x in arg if not x.isspace()]
        for x in arg:
            if x in capital_cities.values():
                print(x, "is the capital of ", end="")
                print(get_key(get_key(x, capital_cities), states))
            else:
                temp = states.get(x)
                if temp != None:
                    print(x, " is the capital of ", capital_cities.get(temp))
                else:
                    print(x ," is neither a capital city nor a state")
