import requests
from bs4 import BeautifulSoup

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
page_text = requests.get(url=url, headers=headers)

page_text.encoding = page_text.apparent_encoding

soup = BeautifulSoup(page_text.text, 'lxml')
li_list = soup.select('.book-mulu > ul > li')
fp = open('./senguo.txt', 'w', encoding='utf-8')
for li in li_list:
	title = li.a.string
	detail_url = 'https://www.shicimingju.com' + li.a['href']
	detail_url = requests.get(url=detail_url, headers=headers, timeout=10)
	
	detail_url.encoding = page_text.apparent_encoding  # 获取编码
	
	detail_soup = BeautifulSoup(detail_url.text, 'lxml')
	div_tag = detail_soup.find('div', class_='chapter_content')
	content = div_tag.text
	fp.write(title + ':' + content + '\n')
	print(title, '爬取成功！！！')
