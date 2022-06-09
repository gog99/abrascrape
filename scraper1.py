import requests, csv
from bs4 import BeautifulSoup

# import pdb;pdb.set_trace()

class FirmInfo:
  def __init__(self, name, addressRegion, county, town, number, url):
    self.name = name.text.strip()
    self.addressRegion = addressRegion.text.strip()
    self.county = county.text.strip()
    self.town = town.text.strip()
    self.number = number.text.strip()
    self.url = url.text.strip()


def getfirmurl
  URL = "http://www.ukaccountingfirms.co.uk/sitemap.xml"
  sitemap = requests.get(URL)
  soup = BeautifulSoup(sitemap.content, "xml.parser")


  # read xml for urls
  # save into a list(?)
  # export


def getfirm():

  firminfos = []
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
