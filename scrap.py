from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import requests


ids = ['b87fd09e',
      'c92e1165',
      '365af238',
      '8bd827f2',
      '3eed90cb',
      '8a3e3a24',
      '4ce5ec07',
      'd3fe7b04',
      '63d21259',
      '69f23665',
      '33d1fc5e',
      'c138c9d3',
      'cd2da935',
      '47c79808',
      '0607d84e',
      '34494647',
      'ff573f21',
      'f26bd1a9',
      '8f51ceb2',
      '56442828',
      '3792d0af',
      'ded5e676',
      '97144f24',
      '1f1894a2',
      '2b056394',
      '25b9fd55',
      '7ee1bb60',
      '27c8844c',
      '54e5acd7',
      '474d4021',
      '8b0eea02',
      '1c84f778',
      'eb88705b',
      '5880900d',
      '51cec9a4',
      '44841822',
      '8cc00f2f',
      'a178719b',
      '0347e675',
      '5977fdc2']


products = []

def fetchData(dealid):
  
  data = requests.get(
  url='https://proxy.scrapeops.io/v1/',
  params={
      'api_key': 'a1d6eab8-f6c9-4841-b1a5-ef632ef28b81',
      'url': 'https://www.amazon.in/deal/{id}'.format(id=dealid),
  },)
  
  soup = BeautifulSoup(data.content, "html.parser")
  links = soup.find_all("a", attrs={'class':'a-size-base a-color-base a-link-normal a-text-normal'})
  titles = soup.find_all('a', attrs={'class':'a-size-base a-color-base a-link-normal a-text-normal'})
  ratings = soup.find_all("span", attrs={'class':'a-icon-alt'})
  total_ratings = soup.find_all("span", attrs={'class':"a-size-small a-color-tertiary"})
  mrps = soup.find_all("span", attrs={'class':'a-size-mini a-color-tertiary octopus-widget-strike-through-price a-text-strike'})
  Selling_Prices = soup.find_all("span", attrs={'class':'a-price-whole'})
  discounts = soup.find_all("div", attrs={'class':'a-size-mini oct-deal-badge-element oct-deal-badge-label'})
  Sellers = soup.find_all("span", attrs={'class':"a-size-base a-color-base a-text-bold"})

  for i in range(len(links)):
    product_link = "https://amazon.in" + links[i].get("href")
    title = titles[i].text.strip()
    mrp = mrps[i].text.strip()
    Selling_Price = Selling_Prices[i].text.strip()
    discount = discounts[i].text.strip()
    Seller = "no seller"
    rating = "no rating"
    total_rating = "no total rating"
    if i < len(ratings):
      rating = ratings[i].text.strip()
      total_rating = total_ratings[i].text.strip()
    
    if i < len(Sellers):
      Seller = Sellers[i].text.strip()
    
    product = {
      'title':title,
      'link':product_link,
      'ratings':rating,
      'total_rating':total_rating,
      'mrp':mrp,
      'Selling price':Selling_Price,
      'discount':discount,
      'seller': Seller
    }
    products.append(product)
    print(product)
    print("\n")

print(len(products))
print("\n")
print(products)

if __name__ == '__main__':
    result =[]
    with ThreadPoolExecutor(max_workers=40) as executor:
        executor.map(fetchData, ids)
  

