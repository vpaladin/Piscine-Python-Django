import requests
import sys
import dewiki

def get_info(arg):
    url = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "parse",
        "page": arg,
        "prop": "wikitext",
        "format": "json",
        "redirects": "true"
    }
    try:
        req = requests.get(url, PARAMS)
        data = req.json()
    except Exception as e:
        print("Not valid requests" + e)
    return (dewiki.from_string(data["parse"]["wikitext"]["*"]))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        text = get_info(sys.argv[1])
        with open(f"{sys.argv[1]}_of_the_search.wiki",'w', encoding=("utf-8")) as f:
            f.write(text)

