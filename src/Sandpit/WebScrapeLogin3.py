import requests
from lxml import html

USERNAME = "masterkcook@hotmail.com"
PASSWORD = "Master2010"

LOGIN_URL = "https://bitbucket.org/account/signin/?next=/"
URL = "https://bitbucket.org/dashboard/repositories"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    print(authenticity_token)

    # Create payload
    payload = {
        "username": USERNAME,
        "password": PASSWORD,
        "csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))

    print(result.ok)  # Will tell us if the last request was ok
    print(result.status_code)  # Will give us the status from the last request

    print(result.content)
    # tree = html.fromstring(result.content)
    # bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    # print(bucket_names)

if __name__ == '__main__':
    main()