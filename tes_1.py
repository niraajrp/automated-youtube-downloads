import requests
from bs4 import BeautifulSoup
from pprint import pprint

def getData():
    url = "https://www.yellowpages.com/search?search_terms=resturant&geo_location_terms=Kathmandu%2C+00"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all("a")
    for link in links:
        print("<a href='%s>%s</a>"%(link.get("href"), link.text))
        pass
    pass

if __name__ == '__main__':
    getData()

