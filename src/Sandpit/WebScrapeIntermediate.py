from bs4 import BeautifulSoup
import requests

r = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
soup = BeautifulSoup(r.text, "lxml")
print(soup.prettify())