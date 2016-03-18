# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-06-19 17:11'

__mail__ = 'gancj@ucweb.com/393037282@qq.com'


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import weiboLogin
import urllib
import urllib2

username = 'yourname'
pwd = 'yourpwd'

WBLogin = weiboLogin.weiboLogin()
WBLogin.login(username, pwd)