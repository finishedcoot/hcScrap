import requests
from bs4 import BeautifulSoup
import pprint

site = requests.get('https://news.ycombinator.com/')
site2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(site.text, 'html.parser')
soup2 = BeautifulSoup(site2.text, 'html.parser')
links = soup.select('.storylink') and soup2.select('.storylink')
subtext = soup.select('.subtext') and soup2.select('.subtext')

def sort_stories_bt_votes(hnlist):
    return sorted(hnlist,key=lambda k:k['points'])

def creat_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        votes = subtext[index].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ""))
            if points > 99:
                hn.append({'title': title, 'link': href, 'points': points})

    return sort_stories_bt_votes(hn)

pprint.pprint(creat_custom_hn(links, subtext))
