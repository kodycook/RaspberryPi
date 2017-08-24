import requests
from bs4 import BeautifulSoup
from lxml import html

class Query():

    def __init__(self, attributes):

        self.logUrl = attributes["logUrl"]
        self.tarUrl = attributes["tarUrl"]
        self.actUrl = attributes["actUrl"]
        self.form = attributes["statAttr"]
        self.authAttr = attributes["authAttr"]
        self.vals = attributes["vals"]
        self.debug = True

    def scrape(self):
        session = requests.session()

        login = session.get(self.logUrl)
        login_html = html.fromstring(login.text)

        if(self.actUrl == ""):
            newUrl = login.url
        else:
            tree = html.fromstring(login.text)
            newUrl = list(set(tree.xpath("//form[@name='{0}']/@action".format(self.actUrl))))[0]


        soup = BeautifulSoup(login.text, 'lxml')
        self.form['hash'] = soup.find_all(attrs={"name" : "hash"})[0].get("value")

        print(self.form)

        # print(newUrl)

        # Perform login
        result = session.post(newUrl, data = self.form, headers = dict(referer = newUrl))
        print(result.headers)

        # Scrape url
        # result = session.get(self.tarUrl, headers = dict(referer = self.tarUrl))

        if self.debug == True:
            print(result.ok)  # Will tell us if the last request was ok
            print(result.status_code)  # Will give us the status from the last request
            print(result.text)

        else:
            tree = html.fromstring(result.text)

            for key, value in self.vals.items():
                scrapedValue = ""
                for i in range(0, len(value)):
                    print(tree.xpath(value[i]))
                    scrapedValue += tree.xpath(value[i])[0].strip()
                    if i != len(value)-1:
                        scrapedValue += " "
                print("{0}: {1}".format(key, scrapedValue))

        session.close()

