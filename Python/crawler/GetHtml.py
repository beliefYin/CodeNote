# -*- coding: utf-8 -*-
import requests

url = "https://search.jd.com/Search?keyword=%E6%89%8B%E5%8A%9E&enc=utf-8&suggest=2.def.0.V01&wq=shouban&pvid=a69d4d9073e843788e37cd721994f92c"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
html = response.text
with open("htmltext.txt", 'w', encoding='utf-8') as f:
	f.write(html)