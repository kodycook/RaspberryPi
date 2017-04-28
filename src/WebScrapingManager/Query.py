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

    # hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
    #
    # # print(hidden_inputs)
    #
    # # Add in hidden attributes to the headers form
    # for x in hidden_inputs:
    #     try:
    #         form = {x.attrib["name"]: x.attrib["value"]}
    #     finally:
    #         break



    # hidden_inputs = login_html.xpath('//html//body//form') #DELETE


    print(form)

    print(newUrl)

    # Perform login
    result = session.post(newUrl, data = form, headers = dict(referer = newUrl))

    # Scrape url
    result = session.get(tarUrl, headers = dict(referer = tarUrl))

    print(result.ok)  # Will tell us if the last request was ok
    print(result.status_code)  # Will give us the status from the last request

    # print(result.text)

    # soup = BeautifulSoup(result.text, 'html.parser')

    # print(soup.prettify())

    # print(soup.title)

    # print(soup.find(
    #     id="ctl00_FormContent_TopNavigationBar_SecureNavigation_AccountsDDL_repeater_ctl00_selectedItemPrimary").string)
    # print(soup.find("div", { "class" : "dl-balance" }).string)
    # print(soup.findAll("span", { "class" : "data-left" }))
    # foundtext = soup.find("h3", text = "TOTAL VALUE", attrs = { "string" : "TOTAL VALUE" })
    # foundtext = soup.find("h3", text = "TOTAL DATA")
    # print(foundtext.findNext('span').string.strip())


    print("\n")

    tree = html.fromstring(result.text)
    val = list(set(tree.xpath('//*[@id="panels"]/div[2]/article/div[1]/div/div/div[2]/p/text()[1]')))[0]
    print(val)

    # for key, value in vals.items():
    #     # if len(value) == 3:
    #     #     # scrapedValue = soup.findAll("span", text = "Account Balance")
    #     if len(value) == 4:
    #         scrapedValue = soup.findAll(value[0], {value[1]: value[2]})[value[3]].find("p")
    #         # scrapedValue = soup.findAll(value[0], {value[1]: value[2]})[value[3]].string.strip()
    #     elif len(value) == 8:
    #         # scrapedValue = soup.findAll(value[0], {value[1]: value[2]})[value[3]].findAll(value[4])[value[5]].string.strip()
    #         scrapedValue = soup.findAll(value[0], {value[1]: value[2]})[value[3]].findAll(value[4], {value[5]:value[6]})[value[7]].string

        print("{0}: {1}".format(key, scrapedValue))

    session.close()

