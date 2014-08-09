#!/usr/bin/env python
# coding: utf-8
import web
import MySQLdb
from logger import *
from config import *
from password import *
from functions import *
import time

session = web.ctx.session

class login:
    def GET(self):
        if session.login == True:
            return render.index(site_prefix, site_title)
        return render.login(site_prefix, site_title)
        
    def POST(self):
        username, pwd = web.input().username, web.input().pwd
        if username != None and pwd != None:
            if PasswordManager().checkPassword(username, pwd):
                session.login = True
                session.username = username
                logger.info("IP: %s USER: %s Login Successful." % (session.ip, username))

                now = time.strftime("%Y-%m-%d %H:%M:%S")
                db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME)
                cursor = db.cursor()
                cmd = "UPDATE user SET lasttime ='%s' WHERE username='%s';" % (now, username)
                cursor.execute(cmd)
                db.close()

                raise web.seeother(site_prefix + "/")
            
        logger.info("IP: %s USER: %s Login Failed." % (session.ip, username))
        return render.message(site_prefix, "登录失败", "用户名或密码错误", "", "_parent", "登录界面", 1)

class noverify:
    def GET(self):
        session.login = True
        session.username = "zlw"
        return render.index(site_prefix, site_title) 
