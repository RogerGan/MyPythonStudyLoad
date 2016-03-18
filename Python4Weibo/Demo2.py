# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-06-18 18:51'

__mail__ = 'gancj@ucweb.com/393037282@qq.com'

from snspy import APIClient
from snspy import TwitterMixin      # suppose you are using Twitter

APP_KEY = '885594759'
APP_SECRET = '2e1e21ee3d40d8267dc675de31fbf5e4'
# CALL_BACK = 'http://bingbingrobot.sinaapp.com/'
CALL_BACK = 'https://api.weibo.com/oauth2/default.html'


client = APIClient(TwitterMixin, app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)