#import Scraper
import Query
# This manager creates a


def makeScraper(name, ID, URL, userTag, passTag, username, password, frequency):
    #scraper = Scraper.scraper(name, ID, URL, username, password, frequency)

    this = {
        'name': name,
        'ID': ID,
        'URL': URL,
        'usernameTag' : userTag,
        'passwordTag' : passTag,
        'username': username,
        'password': password,
        'frequency': frequency,
        "active" : True
    }
    return this


internetUsage = makeScraper("Internet Usage",
                            1,
                            "https://toolbox3.iinet.net.au/login",
                            "",
                            "",
                            "",
                            "",
                            24
                            )
phoneUsage = makeScraper("Mobile Usage",
                         2,
                         "https://www.virginmobile.com.au/signon/virginmobile/MyAccount.sec?",
                         "PASSWORD",
                         "USER",
                         "masterkcook@hotmail.com",
                         "Master2010",
                         24
                         )

#print(phoneUsage["URL"])
print(phoneUsage["username"])
Query.scrape(phoneUsage["URL"], phoneUsage["usernameTag"], phoneUsage["passwordTag"], phoneUsage["username"], phoneUsage["password"])

