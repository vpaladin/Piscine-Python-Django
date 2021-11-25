import sys
import requests
from bs4 import BeautifulSoup

def road_to_filosophy(arg):
    list_of_the_departed = []
    list_arg=[]
    url = "https://en.wikipedia.org/wiki/" + arg
    while(True):
        if url not in list_of_the_departed:
            list_of_the_departed.append(url)
            list_arg.append(arg)
        else:
            print("infinite cycle")
            return
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        find_body = soup.find('div', {'class': 'mw-parser-output'}).select("p > a")
        arg = find_body[0].get("title")
        if arg == "Philosophy":
            # print("finally")
            list_arg.append(arg)
            [print(i) for i in list_arg]
            return
        url = "https://en.wikipedia.org/wiki/" + arg.replace(' ', '_')


if __name__ == "__main__":
    if len(sys.argv) == 2:
        road_to_filosophy(sys.argv[1].strip())
