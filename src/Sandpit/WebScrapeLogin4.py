import requests
from lxml import html

USERNAME = "masterkcook@hotmail.com"
PASSWORD = "Master2010"

LOGIN_URL = "https://www.virginmobile.com.au/signon/virginmobile/MyAccount.sec?TYPE=33554433&REALMOID=06-f4d534ec-0b9f-46e4-ba70-0c95eb71c44b&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-wV0F3UxeDtkVQwAP9tgxWBkJlzSUGCHjpj5KuVKWLyEdW9ImxyCl6Wi%2byI2VpGfr3lmjvdxBBD8GKgAtWqW1Mjw0ok%2fEKu%2fL&TARGET=-SM-https%3a%2f%2fwww%2evirginmobile%2ecom%2eau%2fmyaccount%2fsecure"
URL = "https://www.virginmobile.com.au/myaccount/secure/Dashboard/"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='smagentname']/@value")))[0]

    print(authenticity_token)

    # Create payload
    payload = {
        "USER": USERNAME,
        "PASSWORD": PASSWORD,
        "smagentname": authenticity_token
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

    # SMENC:ISO-8859-1
    # SMLOCALE:US-EN
    # target:https://www.virginmobile.com.au/myaccount/secure
    # smauthreason:0
    # smagentname:wV0F3UxeDtkVQwAP9tgxWBkJlzSUGCHjpj5KuVKWLyEdW9ImxyCl6Wi+yI2VpGfr3lmjvdxBBD8GKgAtWqW1Mjw0ok/EKu/L
    # PASSWORD:Master2010
    # USER:masterkcook@hotmail.com
    # ReturnUrl:/MyAccount/Dashboard
    # txtLogin:masterkcook@hotmail.com
    # txtPassword:Master2010
    # "https://www.virginmobile.com.au/signon/virginmobile/MyAccount.sec?TYPE=33554433&REALMOID=06-f4d534ec-0b9f-46e4-ba70-0c95eb71c44b&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-wV0F3UxeDtkVQwAP9tgxWBkJlzSUGCHjpj5KuVKWLyEdW9ImxyCl6Wi%2byI2VpGfr3lmjvdxBBD8GKgAtWqW1Mjw0ok%2fEKu%2fL&TARGET=-SM-https%3a%2f%2fwww%2evirginmobile%2ecom%2eau%2fmyaccount%2fsecure"