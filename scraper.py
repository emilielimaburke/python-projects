from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.amazon.com/s/field-keywords=protein+powder"
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

items = soup.find_all('li', 's-result-item')

csvfile = open('scraper_data.csv', 'a')
writer = csv.writer(csvfile)

for item in items:
	name = item.find('h2').text
	currency = item.find('sup', 'sx-price-currency').text
	whole = item.find('span', 'sx-price-whole').text
	fractional = item.find('sup', 'sx-price-fractional').text
	writer.writerow([name, currency, whole, fractional])
