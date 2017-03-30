import requests

def scrape(logUrl, tarUrl, tags, heads):


    print(logUrl)

    with requests.session() as c:
        print(tarUrl)
        #c.get(logUrl)
        #c.post(logUrl, data=tags, headers=heads)
        #print(c.cookies[''])
        #c.post(logUrl, data=tags)
        #page = c.get(tarUrl)
        #print(page.content)

    #r = requests.post(URL, data=tags)
    #print(r.content)