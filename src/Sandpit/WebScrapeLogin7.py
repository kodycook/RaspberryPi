# THIS SCRIPT PARSES THE QANTAS FREQUENT FLYER DASHBOARD

import requests
from lxml import html

USERNAME = "1915003469"
NAME = "Cook"
PASSWORD = "0951"

LOGIN_URL = "https://www.qantas.com/fflyer/dyn/program/welcome"
URL = "https://www.qantas.com/fflyer/do/dyns/auth/youraccount/yourAccount"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)

    NEW_LOGIN_URL = result.url

    tree = html.fromstring(result.text)
    # authenticity_token = list(set(tree.xpath("//input[@name='smagentname']/@value")))[0]

    # print(authenticity_token)

    # Create payload
    payload = {
        "memberId": USERNAME,
        "lastName": NAME,
        "pin": PASSWORD,
        "deviceFP": "1708fec0cf8bd8474697ad6499d60058"
    }

    # Perform login
    result = session_requests.post(NEW_LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))

    print(result.ok)  # Will tell us if the last request was ok
    print(result.status_code)  # Will give us the status from the last request

    print(result.text)
    # tree = html.fromstring(result.content)
    # bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    # print(bucket_names)

if __name__ == '__main__':
    main()


    # {memberId: "1915003469", pin: "0951", lastName: "Cook", rememberMyDetails: false,…}
    # deviceFP:"1708fec0cf8bd8474697ad6499d60058"
    # lastName:"Cook"
    # memberId:"1915003469"
    # pin:"0951"
    # rememberMyDetails:false