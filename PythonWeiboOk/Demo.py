# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-06-19 17:41'

__mail__ = 'gancj@ucweb.com/393037282@qq.com'


#coding:utf-8
import requests
import base64
import re
import urllib
import rsa
import json
import binascii
import time
username = 'yourname'
password = 'yourpwd'
session = requests.Session()
# url_prelogin = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.5)&_=1364875106625'
url_prelogin = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=' + username + \
     '&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.11)'

url_login = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.5)'
#get servertime,nonce, pubkey,rsakv
resp = session.get(url_prelogin)
json_data  = re.search('\((.*)\)', resp.content).group(1)
data       = json.loads(json_data)
servertime = data['servertime']
nonce      = data['nonce']
pubkey     = data['pubkey']
rsakv      = data['rsakv']
# calc su
su  = base64.b64encode(urllib.quote(username))
#calc sp
rsaPublickey= int(pubkey,16)
key = rsa.PublicKey(rsaPublickey,65537)
message = str(servertime) +'\t' + str(nonce) + '\n' + str(password)
sp = binascii.b2a_hex(rsa.encrypt(message,key))
postdata = {
                    'entry': 'weibo',
                    'gateway': '1',
                    'from': '',
                    'savestate': '7',
                    'userticket': '1',
                    'ssosimplelogin': '1',
                    'vsnf': '1',
                    'vsnval': '',
                    'su': su,
                    'service': 'miniblog',
                    'servertime': servertime,
                    'nonce': nonce,
                    'pwencode': 'rsa2',
                    'sp': sp,
                    'encoding': 'UTF-8',
                    'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
                    'returntype': 'META',
                    'rsakv' : rsakv,
                    }
resp = session.post(url_login,data=postdata)
login_url = re.findall('replace\("(.*)"\)',resp.content)
#print login_url
print resp.content
resp = session.get(login_url[0])
#print resp.content
uid = re.findall('"uniqueid":"(\d+)",',resp.content)[0]
#print uid
#url = "http://weibo.com/u/"+uid
#resp = session.get(url)
#print resp.content
def decode_content(content):
        result = re.findall('<script>STK && STK.pageletM && STK.pageletM.view\((.*?)\)<\/script>',content)
        for i in result:
                r = i.encode("utf-8").decode('unicode_escape').encode("utf-8")
                print r.replace("\/","/")
#url_search = "http://s.weibo.com/weibo/%s?topnav=1&wvr=5&b=1" % "php"
#resp = session.get(url_search)
#decode_content( resp.content )
def add_new(content,resp):
        add_url  = "http://weibo.com/aj/mblog/add?_wv=5&__rnd=%s770"% int(time.time())
        add_data = {
                'text':content,
                'rank':0,
                'rankid':'',
                'location':'home',
                'module':'stissue',
                "hottopicid":"",
                '_surl':'',
                'pic_id':'',
                '_t':0,
                }
        headers={}
        headers ['set-cookie']= resp.headers['set-cookie']
        headers['Referer'] = 'http://weibo.com/u/'+uid+'?topnav=1&wvr=5'
        resp = session.post(add_url,data=add_data,headers=headers)
        print resp.status_code
add_new("hello",resp)
