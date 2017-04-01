#import Scraper
import Query
# This manager creates a


def makeScraper(name, id, url, userTag, userPass, user, password, frequency):
    #scraper = Scraper.scraper(name, ID, URL, username, password, frequency)

    this = {
        'name': name,
        'ID': id,
        'url': url,
        'userTag': userTag,
        'userPass': userPass,
        'user': user,
        'password': password,
        'frequency': frequency,
        'active': True
    }
    return this


internetUsage = makeScraper("Internet Usage",
                            1,
                            "https://toolbox3.iinet.net.au/login",
                            "Username",
                            "Password",
                            "thecooks5@ozemail.com.au",
                            "family5",
                            24
                            )
phoneUsage = makeScraper("Mobile Usage",
                         2,
                         "https://www.virginmobile.com.au/signon/virginmobile/MyAccount.sec?",
                         "USER",
                         "PASSWORD",
                         "masterkcook@hotmail.com",
                         "Master2010",
                         24
                         )

banking = makeScraper("Bank",
                      2,
                      "https://www.bendigobank.com.au/eai/Logon/login.page",
                      "logonForm:username",
                      "logonForm:password",
                      "1625014401",
                      "master21",
                      24
                      )
#
# movies = makeScraper("Mobile Usage",
#                          2,
#                          "http://www.primewire.ag/",
#                          "http://www.primewire.ag/",
#                          {},
#                          {},
#                          24
#                          )

yelp = makeScraper("Yelp",
                         5,
                         "https://www.yelp.com.au/login",
                         "email",
                         "password",
                         "masterkcook@hotmail.com",
                         "master2010",
                         24
                         )

arduino = makeScraper("Yelp",
                         6,
                         "https://id.arduino.cc/auth/login/?go=1",
                         "username",
                         "password",
                         "kodycook",
                         "master",
                         24
                         )




#print(phoneUsage["URL"])
# Query.scrape(internetUsage["url"], internetUsage["userTag"], internetUsage["userPass"], internetUsage["user"], internetUsage["password"])
# Query.scrape(phoneUsage["url"], phoneUsage["userTag"], phoneUsage["userPass"], phoneUsage["user"], phoneUsage["password"])
# Query.scrape(yelp["url"], yelp["userTag"], yelp["userPass"], yelp["user"], yelp["password"])
# Query.scrape(banking["url"], banking["userTag"], banking["userPass"], banking["user"], banking["password"])
Query.scrape(arduino["url"], arduino["userTag"], arduino["userPass"], arduino["user"], arduino["password"])
