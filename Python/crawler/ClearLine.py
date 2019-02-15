# coding = utf-8
import re
def clearBlankLine():
    matchStr = r'^[\t\s]*\n'
    file1 = open('htmltext.txt', 'r', encoding='utf-8') # 要去掉空行的文件 
    file2 = open('text2.txt', 'w', encoding='utf-8') # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if re.match(matchStr, line):
                line = ""
            file2.write(line)
    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    clearBlankLine()