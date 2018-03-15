# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')

import re

str = "['<td>\n291735 addresses\n</td>']"

results = re.search('(\d+)', str).group()

print(type(results))
