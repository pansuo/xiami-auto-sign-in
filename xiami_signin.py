#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
多账户虾米自动签到器
* 请在http://python.org/getit/ 下载python3.


author: kk(fkfkbill@gmail.com)
'''

import sys,os
from datetime import datetime

from urllib.request import urlopen,install_opener,build_opener,Request,HTTPHandler,HTTPCookieProcessor
from http.cookiejar import CookieJar
from urllib.parse import urlencode


#在此填写账户名（可多账户）
user_info=[
	{"email":"","password":""},
]


#xiami uris
site_urls={
  "index":r"",
  "login":r"",
  "signin":r"",
}

#login form without email and password
login_form={
	"done":"/",
	"submit":"登 录",
}

#flags
site_flags={
  "logged-in":r"",
}



#======================================
def login(id,password):
	'''
login xiami.
arugments:
	id: user name or email address
  password: key to login
return:
	url opener:when succeeded
'''
	cookie_support= HTTPCookieProcessor(CookieJar())
	opener = build_opener(cookie_support, HTTPHandler)
	install_opener(opener)

	headers={
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Cache-Control":"max-age=0",
		"Connection":"keep-alive",
		"Content-Length":92,
		"Content-Type":"application/x-www-form-urlencoded",
		"Host":"www.xiami.com",
		"Origin":"http://www.xiami.com",
		"Referer":"http://www.xiami.com/",
		"User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
	}

	req=Request(url=site_urls["login"],
			data=urlencode(user_info).encode("utf-8"),
			headers=headers)
	content=urlopen(req).read()
	
	#===search for sign
	if content.decode("utf-8").find(login_sign)!=-1:
		return opener
	return False
