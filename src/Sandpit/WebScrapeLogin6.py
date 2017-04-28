# THIS SCRIPT PARSES THE VIRGIN FREQUENT FLYER DASHBOARD

import requests
from lxml import html

USERNAME = "1033332194"
PASSWORD = "master"

LOGIN_URL = "https://www.velocityfrequentflyer.com/content/sso/login"
URL = "https://www.velocityfrequentflyer.com/content/MyAccount/"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)

    tree = html.fromstring(result.text)
    # authenticity_token = list(set(tree.xpath("//input[@name='smagentname']/@value")))[0]


    temp = list(set(tree.xpath("//form[@name='velocityForm']/@action")))

    NEW_LOGIN_URL = temp[0]


    print(NEW_LOGIN_URL)

    # Create payload
    payload = {
        "username": USERNAME,
        "password": PASSWORD
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

    # username:1033332194
    # password:master"