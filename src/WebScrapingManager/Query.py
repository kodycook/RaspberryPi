import requests
from lxml import html
import sys

def scrape(url, userTag, passTag, user, password):


    print(url)

    # session = requests.session(config={'verbose': sys.stderr})
    session = requests.session()


    login = session.get(url)
    login_html = html.fromstring(login.text)

    # print(login.text)

    hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')

    # print(hidden_inputs)

    form = dict
    for x in hidden_inputs:
        try:
            form = {x.attrib["name"]: x.attrib["value"]}
        finally:
            break



    # hidden_inputs = login_html.xpath('//html//body//form') #DELETE


    form[userTag] = user
    form[passTag] = password

    print(form)

    response = session.post(url, data=form)

    print(response.text)

    #login_html = html.fromstring(response.text)

    # hidden_inputs = login_html.xpath('//html//body//form')

    # print(hidden_inputs[0].attrib["action"])

    # print(response.text)

    # response = c.get(hidden_inputs[0].attrib["action"])

    # print(response.url)
    # print(response.text)


    session.close()

