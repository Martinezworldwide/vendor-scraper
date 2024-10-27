import requests
from bs4 import BeautifulSoup

def scrape_store(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        products = []

        for product in soup.find_all('div', class_='product-class'):
            name = product.find('h2', class_='product-name').text
            price = product.find('span', class_='product-price').text
            link = product.find('a', class_='product-link')['href']
            affiliate_link = add_affiliate_id(link)
            products.append({'name': name, 'price': price, 'affiliate_link': affiliate_link})
        return products
    else:
        return []

def add_affiliate_id(link):
    affiliate_id = 'your_affiliate_id'
    return f"{link}?aff_id={affiliate_id}"
