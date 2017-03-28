from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()
url = "http://www.pythonforbeginners.com"

r = http.request('GET', 'http://econpy.pythonanywhere.com/ex/001.html')

soup = BeautifulSoup(r.data.decode('utf-8'),"lxml")

print(soup.prettify())