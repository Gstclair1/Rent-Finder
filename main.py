from bs4 import BeautifulSoup
import requests

RENTAL_LISTINGS_LINK = "https://www.zillow.com/phoenix-az/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Phoenix%2C%20AZ%22%2C%22mapBounds%22%3A%7B%22west%22%3A-113.07262180078125%2C%22east%22%3A-111.17748019921875%2C%22south%22%3A32.983849208163804%2C%22north%22%3A34.22367564471628%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A40326%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A537596%7D%2C%22mp%22%3A%7B%22max%22%3A2400%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%7D"
GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSc8YraIUB38grEbBWT7STNvxKwvXTr6s8mQUSyFm57Wadiu7w/viewform?usp=sf_link"
BROWSER_HEADER = {
    "Accept-Language": "en-US",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
}

response = requests.get(url=RENTAL_LISTINGS_LINK, headers=BROWSER_HEADER)
soup = BeautifulSoup(response.text, 'html.parser')
links = []
for link in soup.find_all('.List-c11n-8-69-2__sc-1smrmqp-0 srp__sc-1psn8tk-0 ckwVds photo-cards with_constellation a'):
    links.append(link.get('href'))

