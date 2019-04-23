#!/usr/bin/env python
## -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re  
import subprocess
from subprocess import Popen, PIPE, call
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
url = "https://1xjet.world/ru/live/Mortal-Kombat/".encode('utf-8')
driver.get(url)

src = driver.page_source.encode('utf-8')
target = "Саб-Зиро"
found = re.search(target,src)
found = bool(found)
print(found)

if bool(found):
	try:
		sdfjdlubprocess.check_call([r"/home/ruzal/test.sh"])
	except (BaseException):
		print 1

driver.close();