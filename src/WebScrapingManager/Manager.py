#import Scraper
import Query
# This manager creates a


def makeScraper(name, id, logUrl, tarUrl, tags, heads, frequency):
    #scraper = Scraper.scraper(name, ID, URL, username, password, frequency)

    this = {
        'name': name,
        'ID': id,
        'logURL': logUrl,
        'tarURL': tarUrl,
        'tags': tags,
        'heads': heads,
        'frequency': frequency,
        'active': True
    }
    return this


internetUsage = makeScraper("Internet Usage",
                            1,
                            "https://toolbox3.iinet.net.au/login",
                            "https://toolbox3.iinet.net.au/",
                            {'ReturnUrl':'',
                             'Username':'thecooks5@ozemail.com.au',
                             'Password':'family5',
                             'action':'Index:'},
                            {},
                            24
                            )
phoneUsage = makeScraper("Mobile Usage",
                         2,
                         "https://www.virginmobile.com.au/signon/virginmobile/MyAccount.sec?",
                         "https://www.virginmobile.com.au/myaccount/secure/",
                         {'SMENC':'ISO-8859-1',
                          'SMLOCALE':'US-EN',
                          'target':'https://www.virginmobile.com.au/myaccount/secure',
                          'smauthreason':'0',
                          'smagentname':'wV0F3UxeDtkVQwAP9tgxWBkJlzSUGCHjpj5KuVKWLyEdW9ImxyCl6Wi+yI2VpGfr3lmjvdxBBD8GKgAtWqW1Mjw0ok/EKu/L',
                          'PASSWORD':'Master2010',
                          'USER':'masterkcook@hotmail.com',
                          'ReturnUrl':'/MyAccount/Dashboard',
                          'txtLogin':'masterkcook@hotmail.com',
                          'txtPassword':'Master2010'
                          },
                         {},
                         24
                         )

#print(phoneUsage["URL"])
Query.scrape(internetUsage["logURL"], internetUsage["tarURL"], internetUsage["tags"], internetUsage["heads"])
#Query.scrape(phoneUsage["logURL"], phoneUsage["tarURL"], phoneUsage["tags"], phoneUsage["heads"])

