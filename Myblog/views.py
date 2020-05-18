import io
import json

import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
from numpy import unicode

bas_url = "https://t.me/Shayari_Ka_Samunder/"
# "https://t.me/c/1213482319/188176"

# ya url mhadhun
# page = requests.get(bas_url + "2777")
# page = requests.get("http://localhost:63342/Sample_Project/templates/sam.html?_ijt=ttb02lamnbv2fls5pglsf22af2")
# page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
# soup = BeautifulSoup(page.content, 'html.parser')
ulss = []
for i in range(1500,1550):
    print(i)
    ulss.append(bas_url + str(i))


#     print(bas_url + str(i), end="\n")
# print(ulss)
# for u in ulss:
#     print(u)
#

# meta
# property="og:description"
def index(request):
    ds = []
    for i, u in enumerate(ulss, start=1):
        page = requests.get(u)
        soup = BeautifulSoup(page.content, 'html.parser')
        job_elems = soup.find('meta', property='og:description')
        ans = job_elems['content'] if job_elems else 'No data Available'
        if ans == "Channel Admin   	@Do_Good_For_Otherss		अपना दर्द सबको न बताएं 	मरहम एक आधे घर में होता है	नमक घर घर में होता है।":
            continue
        print(i, ans, i,ans)
        ds.append({i: ans})
    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str
    with io.open('data1.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(ds,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

    # print(ds)
    data = {"•✤┈•शायरी का समुद्र•┈✤•": ds, }
    return JsonResponse(data=data)

    # job_elems = soup.find('meta', property='og:description')
    # ans = job_elems['content'] if job_elems else 'No data Available'
    # data = {
    #     "ans": ans,
    #     "sh": job_elems.prettify(),
    #     "main": soup.prettify()
    # }
    # return JsonResponse(data=data)


def home(request):
    # page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
    # soup = BeautifulSoup(page.content, 'html.parser')
    # title of the page
    # print(soup.title)
    #
    # # get attributes:
    # print(soup.title.name)
    #
    # # get values:
    # print(soup.title.string)
    #
    # # beginning navigation:
    # print(soup.title.parent.name)
    #
    # # getting specific values:
    # print(soup.p)
    # •✤┈• जब गाँव में था, पूरा गाँव मेरा था •┈✤•
    # •✤┈• अब सिर्फ एक घर है, शहर में मेरा  •┈✤•
    # print(soup.find_all('p'))
    #
    # for paragraph in soup.find_all('p'):
    #     print(paragraph.string)
    #     print(str(paragraph.text))
    # # soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    # # soup.find_all('p', class_='outer-text')
    # all_p = soup.find_all('p')
    data = {
        "home": {
            "firt": "https://t.me/Shayari_Ka_Samunder/2777",
            "shayri": "    •✤┈• जब गाँव में था, पूरा गाँव मेरा था •┈✤• \n    •✤┈• अब सिर्फ एक घर है, शहर में मेरा  •┈✤•",
            "Sample": "This Is a main page og my life"
        },
        # "all_data": {
        #     "title_of_the_page": soup.title,
        # "get_attributes": soup.title.name,
        # "get_values": soup.title.string,
        # "beginning_navigation": soup.title.parent.name,
        # "all_p": soup.find_all('p'),
        # "getting_specific_values": soup.p,
        # "main": soup.prettify(),
        # },
        "about": "This is a HOme Page About My Link To other as a Page"
    }
    return JsonResponse(data=data)
