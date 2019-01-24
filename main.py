from lxml import html
import requests

url = "https://www.glassdoor.com/Job/operation-research-analyst-jobs-SRCH_KO0,26_IP3.htm"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like

page = requests.get(url, headers=headers)
tree = html.fromstring(page.content)
print(page.content)

data = tree.xpath('//*[@id="JobDesc3081549158"]/div/text()[2]')
print(data)