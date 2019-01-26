from lxml import html
from requests import get
from bs4 import BeautifulSoup

url = "https://www.indeed.com/viewjob?jk=1fedc0d304417c06&tk=1d2105cgi5hhb804&from=serp&vjs=3"
headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
response = get(url, headers=headers)
# tree = html.fromstring(response.content)
# data = tree.xpath('//*[@id="MainCol"]/div/ul/li[1]/div[2]/div[1]/div[1]/a')
# print(response.text[:100])

html_soup = BeautifulSoup(response.text, 'html.parser')
jobs_desc = html_soup.find_all('p')

# Remove all the html tag from the result
for i in range(0, len(jobs_desc)):
    # jobs_desc[i].replace('<p>','')
    # jobs_desc[i].replace('</p>','')
    # jobs_desc[i].replace('<b>','')
    # jobs_desc[i].replace('</b>','')
    print(jobs_desc[i].string)
    #print(type(jobs_desc[1].string))
