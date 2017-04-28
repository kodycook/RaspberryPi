#import Scraper
import Query
# This manager creates a

# TODO: Add a string to search to confirm successful login, eg. "Kody Cook"

def makeScraper(name, id, logUrl, tarUrl, actUrl, statAttr, authAttr, vals, frequency):
    #scraper = Scraper.scraper(name, ID, URL, username, password, frequency)

    this = {
        'name': name,
        'ID': id,
        'logUrl': logUrl,
        'tarUrl': tarUrl,
        'actUrl': actUrl,
        'statAttr': statAttr,
        'authAttr': authAttr,
        'vals': vals,
        'frequency': frequency,
        'active': True
    }
    return this

# The Structure of a scraper is as follows: (Name <String>,
#                                           ID number <int>,
#                                           Login Url <String>,
#                                           Target Url <String>,
#                                           URL in Action Form,
#                                           Static Form Attributes {Password Name <String>: Password Value <String>, ...},
#                                           Parsed Auth Attributes {Auth Name <String>: Auth Value <String>, ...},
#                                           Values of Interest {Value Name <String>: Http Path <String>, ...},
#                                           Daily Number of Scrapes <int>
#                                           }

internetUsage = makeScraper(
    "Internet Usage",
    1,
    "https://toolbox3.iinet.net.au/login",
    "https://toolbox3.iinet.net.au",
    "",
    {'ReturnUrl':'',
     'Username':'thecooks5@ozemail.com.au',
     'Password':'family5',
     'action:Index':''},
    {},
    {"Account Balance": ["div", "class", "dl-balance", 0, "span", "", "", 1],
        "Remaining Internet": ["div", "class", "ub-bar multiple", 0]},
    24
)

# , "p", "class", "usage-text", 0

phoneUsage = makeScraper(
    "Mobile Usage",
    2,
    "https://www.virginmobile.com.au/signon/virginmobile/MyAccount.sec?",
    "https://www.virginmobile.com.au/myaccount/secure/Dashboard/",
    "",
    {'USER':'masterkcook@hotmail.com',
     'PASSWORD':'Master2010'},
    {},
    {'Phone Usage': ["span", "class", "data-left", 0],
     'Data Usage': ["span", "class", "data-left", 1]},
    24
)

# banking = makeScraper("Bank",
#                       2,
#                       "https://www.bendigobank.com.au/eai/Logon/login.page",
#                       "logonForm:username",
#                       "logonForm:password",
#                       "1625014401",
#                       "master21",
#                       24
#                       )

virgin = makeScraper(
    "Virgin Frequent Flyer",
    4,
    "https://www.velocityfrequentflyer.com/content/sso/login",
    "https://www.velocityfrequentflyer.com/content/MyAccount/",
    "velocityForm",
    {'username':'1033332194',
     'password':'master'},
    {},
    {},
    6
)

# qantas = makeScraper(
#     "Virgin Frequent Flyer",
#     5,
#     "",
#     "",
#     {'username':'1033332194',
#      'password':'master'},
#     {},
#     {},
#     6
# )

#
# # movies = makeScraper("Movies",
# #                          2,
# #                          "http://www.primewire.ag/",
# #                          "http://www.primewire.ag/",
# #                          {},
# #                          {},
# #                          24
# #                          )
#
# yelp = makeScraper("Yelp",
#                          5,
#                          "https://www.yelp.com.au/login",
#                          "email",
#                          "password",
#                          "masterkcook@hotmail.com",
#                          "master2010",
#                          24
#                          )
#
# arduino = makeScraper("Arduino",
#                          6,
#                          "https://id.arduino.cc/auth/login/?go=1",
#                          "username",
#                          "password",
#                          "kodycook",
#                          "master",
#                          24
#                          )




#print(phoneUsage["URL"])
Query.scrape(internetUsage)
# Query.scrape(phoneUsage)
# Query.scrape(virgin)
