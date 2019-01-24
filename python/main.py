from lxml import html
from requests import get
from bs4 import BeautifulSoup

url = "https://www.indeed.com/q-Job-Find-jobs.html"
headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
response = get(url, headers=headers)
# tree = html.fromstring(response.content)
# data = tree.xpath('//*[@id="MainCol"]/div/ul/li[1]/div[2]/div[1]/div[1]/a')
#print(response.text[:100])

html_soup = BeautifulSoup(response.text, 'html.parser')
jobs_desc = html_soup.find_all('span', class_='summary')
print(jobs_desc[:100])
