#!/usr/bin/env python
# coding: utf-8
import web
import MySQLdb
from logger import *
from config import *
from functions import *
import time

session = web.ctx.session

class MakeTop:
    def GET(self):
        name = getTruename(session.username)
        return render.top(site_prefix, name)

class MakeMenu:
    def GET(self):
        menus = self.getFunctions()
        return render.menu(site_prefix, menus)

    def getFunctions(self):
        db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME, charset='utf8')
        cursor = db.cursor()
        cmd = 'SELECT * FROM functions;'
        cursor.execute(cmd)
        rows = cursor.fetchall()
        result = []
        if rows == None:
            return result
        for each in rows:
            everyone = {}
            everyone['name'] = each[1]
            everyone['url'] = each[2]
            result.append(everyone)
        db.close()
        return result

class welcome:
    def GET(self):
        username = session.username
        name = getTruename(session.username)
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME, charset='utf8')
        cursor = db.cursor()
        cmd = 'SELECT registertime,lasttime FROM user WHERE username="%s";' % username
        cursor.execute(cmd)
        rowUser = cursor.fetchone()
        db.close()
        registertime = rowUser[0]
        logintime = rowUser[1]
        ip = session.ip
        return render.welcome(site_prefix, username, name, now, registertime, logintime, ip)
