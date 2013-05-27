#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
multi-account auto xiami signin tool
python3 required, download at http://python.org/getit/


author: kk(fkfkbill@gmail.com)
'''

import sys,os
from datetime import datetime

from urllib.request import urlopen,install_opener,build_opener,Request,HTTPHandler,HTTPCookieProcessor
from http.cookiejar import CookieJar
from urllib.parse import urlencode


#在此填写账户名（可多账户）
#put ur account(s) here
user_info=[
("",""),
]


#xiami uris
site_urls={
  "index":r"",
  "login":r"",
  "signin":r"",
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
			"Host":"www.xiami.com",
			"Origin":"http://www.xiami.com",
			"Referer":"",
			"User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
	}

	req=Request(url=site_urls["login"],
			data=urlencode(user_info).encode("utf-8"),
			headers=headers)
	content=urlopen(req).read()
	
	#===search for sign
	if content.decode("gbk").find(login_sign)!=-1:
		return opener
	return False
