from lxml import html
from requests import get
from bs4 import BeautifulSoup
import csv
from getPageElement import getContent


web_prefix = "https://www.indeed.fi"
url = "https://www.indeed.fi/jobs?q=operations&l=Vaasa"
headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

response = get(url, headers=headers)
html_soup = BeautifulSoup(response.text, 'html.parser')

# Get the divs that content the jobs
jobs_link_div  = html_soup.find_all('div',class_ = "jobsearch-SerpJobCard")

# Get the links from the divs
job_links = []
job_title = []
for i in range(0, len(jobs_link_div)):
    job_links.append(jobs_link_div[i].find_all('a')[0]['href'])
    job_title.append(jobs_link_div[i].find_all('a')[0]['title'])
print(job_title[1])

#Travel all the pages:
for i in range(0, len(job_links)):
    link = web_prefix + job_links[i]
    response = getContent(url=link, headers=headers)
    print(response)
    break

