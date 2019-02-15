import re
from xlwt import Workbook


def main():
	book = Workbook()
	sheet = book.add_sheet("手办")
	sheet.write(0,0,"名字")
	sheet.write(0,1,"价格")
	sheet.write(0,2,"链接")
	book.save('京东数据.xls')

	with open("htmltext.txt", 'r', encoding='utf-8') as f:
		html = f.read()
	sMatchMoney = r'<em>￥</em><i>(.+?)</i>'

#<em>漫威卡通蜘蛛侠小号摆件车内摆件复仇者联盟3机箱<font class="skcolor_ljg">手办</font>漫威动漫模型<font class="skcolor_ljg">手办</font>汽车摆件2.5英寸正版漫威新款</em>


	sMatchName = r'<em>(.+?)</em>[\n\t]*<i class="pr'
	clear = r'((.*?)<font class="skcolor_ljg">(.*?)</font>)+'
	moneys = re.findall(sMatchMoney, html)
	names = re.findall(sMatchName, html)
	i = 0
	for j in names:
		tmp = re.findall(clear, names[i])
		tmp = tmp[0]
		tmp = tmp[1:-1]
		tmpName = ""
		for name in tmp:
			tmpName = tmpName + name
		names[i] = tmpName
		i = i + 1

	i = 0
	for money in moneys:
		i = i + 1
		sheet.write(i, 0, names[i-1])
		sheet.write(i, 1, money)
	book.save('京东数据.xls')

if __name__ == '__main__':
	main()



