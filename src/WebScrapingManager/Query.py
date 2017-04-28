import requests
from lxml import html
from bs4 import BeautifulSoup

def scrape(attributes):

    logUrl = attributes["logUrl"]
    tarUrl = attributes["tarUrl"]
    actUrl = attributes["actUrl"]
    form = attributes["statAttr"]
    authAttr = attributes["authAttr"]
    vals = attributes["vals"]


    session = requests.session()

    login = session.get(logUrl)
    login_html = html.fromstring(login.text)

    if(actUrl == ""):
        newUrl = login.url
    else:
        tree = html.fromstring(login.text)
        newUrl = list(set(tree.xpath("//form[@name='{0}']/@action".format(actUrl))))[0]



    # print(form)

    # print(newUrl)

    # Perform login
    result = session.post(newUrl, data = form, headers = dict(referer = newUrl))

    # Scrape url
    result = session.get(tarUrl, headers = dict(referer = tarUrl))

    # print(result.ok)  # Will tell us if the last request was ok
    # print(result.status_code)  # Will give us the status from the last request

    # print(result.text)

    # print("\n")

    tree = html.fromstring(result.text)

    for key, value in vals.items():
        scrapedValue = tree.xpath(value[0])[0].strip()
        print("{0}: {1}".format(key, scrapedValue))

    session.close()

