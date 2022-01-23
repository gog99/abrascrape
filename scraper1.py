import requests, csv
from bs4 import BeautifulSoup

# import pdb;pdb.set_trace()
# region and county code here

URL = "http://www.ukaccountingfirms.co.uk/bishop-auckland/"
page = requests.get(URL)

class FirmInfo:
  def __init__(self, name, addressRegion, county, town, number, url):
    self.name = name.text.strip()
    self.addressRegion = addressRegion.text.strip()
    self.county = county.text.strip()
    self.town = town.text.strip()
    self.number = number.text.strip()
    self.url = url.text.strip()


def getfirm():
  firminfos = []
  soup = BeautifulSoup(page.content, "html.parser")
  firm_cards = soup.find_all(class_="card")

  for firm_card in firm_cards:
    firm_name = firm_card.find("span", itemprop="name")
    firm_addressRegion = firm_card.find("span", itemprop="addressRegion")
    firm_county = firm_card.find("a", href="/county-durham/")
    firm_town = firm_card.find("span", itemprop="addressLocality")
    firm_number = firm_card.find("span", itemprop="telephone")
    firm_url = firm_card.find("h3", class_="card-heading")
    firminfo = FirmInfo(
      firm_name, firm_addressRegion, firm_county, firm_town, firm_number,
      firm_url
    )
    firminfos.append(firminfo)

  return firminfos


if __name__ == '__main__':
  firms = getfirm()
  for firm in firms:
    print(
      firm.name, firm.addressRegion , firm.county, firm.town, firm.number,
      firm.url
    )
    print(f'Name: {firm.name},\nCounty: {firm.county}')




# for each region's countys, find each town's firms card
# for each card find the name, region, county, town, number, description
# save in a database
# export database to .csv
