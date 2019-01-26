from lxml import html
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from getPageElement import getContent


web_prefix = "https://www.indeed.com"
url = "https://www.indeed.com/jobs?q=operations&l=New+York%2C+NY"
headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

response = get(url, headers=headers)
html_soup = BeautifulSoup(response.text, 'html.parser')

# Get the divs that content the jobs
jobs_link_div  = html_soup.find_all('div',class_ = "jobsearch-SerpJobCard")

# Get the links from the divs
job_links = []
job_title = []
for i in range(0, len(jobs_link_div)):
    temp = jobs_link_div[i].find_all('a')[0]
    job_links.append(web_prefix+ temp['href'])
    job_title.append(temp['title'])

#Travel all the pages:
data_list = []
#print(job_links)
for i in range(0, len(job_links)):
    link = job_links[i]
    response = getContent(url=link, headers=headers)
    data_list.append(response)

print(data_list[1])
df = pd.DataFrame({'Job title':job_title, 'Description':data_list, 'Link': job_links})
writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
