import requests
from bs4 import BeautifulSoup

URL = "http://www.ukaccountingfirms.co.uk/bishop-auckland/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
cardstart = soup.find(id="pListing")
firmcards = cardstart.find_all("div", class_="navmenu-left")

for firmcard in firmcards:
  print(firmcard)

# class="navmenu-left"

# for firmcard in firmcard:
#    print(firmcard, end="\n"*2)
