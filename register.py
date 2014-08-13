#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import MySQLdb
from logger import *
from config import *
from password import *
import time

session = web.ctx.session

class Register():
    def GET(self):
        return render.register(site_prefix, "新用户注册")

    def POST(self):
        username = web.input().username
        password = web.input().newpw
        name = web.input().name
        crypted = PasswordManager().encrypt_server_password(password)
        
        db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME, charset='utf8')
        cursor = db.cursor()
        cmd = "SELECT username FROM user WHERE username='%s';" % username
        cursor.execute(cmd)
        rowUser = cursor.fetchall()
        
        if len(rowUser) != 0:
            db.close()
            logger.info("IP: %s USER: %s sign up failed." % (session.ip, username))
            return render.message(site_prefix, "注册失败", "该用户已经存在", "register", "_parent", "重新注册")
        else:
            now = time.strftime("%Y-%m-%d %H:%M:%S")
            cmd = "INSERT INTO user (`username`, `password`, `name`, `registertime`) VALUES ('%s', '%s', '%s', '%s');" % (cleanString(username), cleanString(crypted), cleanString(name), now)
            cursor.execute(cmd)
            db.close()
            logger.info("IP: %s USER: %s sign up success." % (session.ip, username))

            session.login = True
            session.username = username
            logger.info("IP: %s USER: %s Login Successful." % (session.ip, username))

            now = time.strftime("%Y-%m-%d %H:%M:%S")
            db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME, charset='utf8')
            cursor = db.cursor()
            cmd = "UPDATE user SET lasttime ='%s' WHERE username='%s';" % (now, username)
            cursor.execute(cmd)
            db.close()

            return render.message(site_prefix, "注册成功", "新用户注册成功，现在将进入系统", "", "_parent", "首页")
