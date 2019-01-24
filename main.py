from lxml import html
import requests

url = "https://www.glassdoor.com/Job/operation-research-analyst-jobs-SRCH_KO0,26_IP3.htm"

page = requests.get(url)
tree = html.fromstring(page.content)

data = tree.xpath('//div[@class="jobDescriptionContent desc"]/text()')
print(data)