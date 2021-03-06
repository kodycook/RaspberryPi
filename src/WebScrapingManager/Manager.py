#!/usr/bin/python
from Query import Query
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
    {'Account Balance': ['/html/body/div[3]/div[1]/div/div[1]/div/div/p/span[1]/text()'],
     'Data Usage': ['//*[@id="panels"]/div[2]/article/div[1]/div/div/div[2]/p/text()',
                    '//*[@id="panels"]/div[2]/article/div[1]/div/div/div[2]/p/abbr[1]/text()',
                    '//*[@id="panels"]/div[2]/article/div[1]/div/div/div[2]/p/text()[2]',
                    '//*[@id="panels"]/div[2]/article/div[1]/div/div/div[2]/p/abbr[2]/text()'],
     'Days Left in Billing Period':['//*[@id="panels"]/div[2]/article/div[1]/div/p/strong[2]/text()']},
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
    {'Account Balance':['//*[@id="ctl00_FormContent_FullContentArea_SidebarTop_ServiceStatusViewSwitcher_ctl00_ControlSwitcher_ctl00_AccountOverviewPostpaidMobile_lblTotalOutstanding"]/text()'],
     'Phone Usage': ['//*[@id="ctl00_FormContent_FullContentArea_TopRowSection_TopRow_ButtonBar_ButtonBarPanelRepeater_ctl01_UsagePostpaidMobile_pnlPostPaidMobile"]/ul/li[1]/strong/span[1]/text()'],
     'Data Usage': ['//*[@id="ctl00_FormContent_FullContentArea_TopRowSection_TopRow_ButtonBar_ButtonBarPanelRepeater_ctl01_UsagePostpaidMobile_pnlPostPaidMobile"]/ul/li[2]/ul/li/strong/span[1]/text()'],
     'Days Left in Billing Period': ['//*[@id="ctl00_FormContent_FullContentArea_TopRowSection_TopRow_ButtonBar_ButtonBarPanelRepeater_ctl01_UsagePostpaidMobile_pnlPostPaidMobile"]/ul/li[3]/ul/li/span/strong/text()']},
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
    {'Frequent Flyer Points':['//*[@id="points-balance"]/div/dl/dd[1]/text()'],
     'Status Points':['//*[@id="points-balance"]/div/dl/dd[2]/text()'],
     'Membership Level':['//*[@id="content-a"]/div[2]/div[1]/div[1]/table/tbody/tr[4]/td/text()'],
     'Renewal Date':['//*[@id="upgradeTierLightbox"]/table[1]/tbody/tr[2]/td[1]/span/text()']},
    6
)

qantas = makeScraper(
    "Qantas Frequent Flyer",
    5,
    "https://api.services.qantasloyalty.com/auth/member/login",
    "https://www.qantas.com/fflyer/do/dyns/auth/youraccount/yourAccount",
    "",
    {'lastName':'COOK',
     'memberId':'1915003469',
     'pin':'0951'},
    {},
    {},
    6
)







print("IINET Internet Usage")
iinetHomeInternet = Query(internetUsage)
iinetHomeInternet.scrape()

print("\n")
print("Virgin Mobile Usage")
virginMobile = Query(phoneUsage)
virginMobile.scrape()

print("\n")
print("Virgin Frequent Flyer")
virginFrequentFlyer = Query(virgin)
virginFrequentFlyer.scrape()

# print("\n")
# print("Qantas Frequent Flyer")
# QantasFrequentFlyer = Query(qantas)
# QantasFrequentFlyer.scrape()