from lxml import html
import requests

url = "https://www.glassdoor.com/Job/operation-research-analyst-jobs-SRCH_KO0,26_IP3.htm"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like

response = requests.get(url, headers=headers)
# tree = html.fromstring(response.content)
# data = tree.xpath('//*[@id="MainCol"]/div/ul/li[1]/div[2]/div[1]/div[1]/a')

print(response.text[:1000])
html_soup = BeautifulSoup(response.text, 'html.parser')

print(tree.tag)