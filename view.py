#!/usr/bin/env python
# coding: utf-8
import web
from logger import *
from config import *
from functions import *
import urllib2

session = web.ctx.session

class view:
    def GET(self):
        if session.login != True:
            return render.message(site_prefix, "未登录", "您尚未登录", "", "_parent", "登录界面")

        devices = getDevices();
        return render.view(site_prefix, devices)

class viewpos:
    def GET(self):
        if session.login != True:
            return render.message(site_prefix, "未登录", "您尚未登录", "", "_parent", "登录界面")
        id = web.input().id
        devices = getDevices(id)
        posname = {}
        for key in devices:
            pos = devices[key][9]
            data = ""
            try:
                lat = pos.split(",")[1]
                lon = pos.split(",")[0]
                baidu_api = "http://api.map.baidu.com/geocoder/v2/?ak=PkztGytCOmGprnY4cIlfamsm&location=%s,%s&output=json&pois=0" % (lat, lon)
                req = urllib2.Request(baidu_api)
                data = urllib2.urlopen(req)
                data = eval(data.read())["result"]["formatted_address"]
            except Exception as e:
                data = "无信息"
                logger.info(e)
            posname[devices[key][0]] = data
        return render.pos(site_prefix, devices, posname)

class viewhispos:
    def GET(self):
        if session.login != True:
            return render.message(site_prefix, "未登录", "您尚未登录", "", "_parent", "登录界面")
        id = web.input().id
        devices = getDevices(id)
        hispos = getHisPos(id)
        return render.hispos(site_prefix, devices, hispos)