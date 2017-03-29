import requests

def scrape(URL, userTag, passTag, username, password):

    values = {userTag : username,
              passTag : password}

    print(URL)
    r = requests.post(URL, data=values)
    print(r.content)