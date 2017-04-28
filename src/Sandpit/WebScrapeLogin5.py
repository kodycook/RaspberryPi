# THIS SCRIPT PARSES THE IINET DASHBOARD

import requests
from lxml import html

USERNAME = "thecooks5@ozemail.com.au"
PASSWORD = "family5"

LOGIN_URL = "https://toolbox3.iinet.net.au/login"
URL = "https://toolbox3.iinet.net.au/"

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
        "ReturnUrl":"",
        "Username": USERNAME,
        "Password": PASSWORD,
        "action:Index":""
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

    # ReturnUrl:
    # Username:thecooks5@ozemail.com.au
    # Password:family5
    # action:Index: