#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from hashlib import sha256
from hmac import HMAC 
import web
from logger import *
from config import *
from functions import *
import MySQLdb

session = web.ctx.session
salt_length = 13

class PasswordManager():
    def encrypt_server_password(self, password, salt = None):
        if salt is None:
            matrix = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~!@#$%^&*"
            salt = ''.join(random.sample(matrix, salt_length))
        
        assert salt_length == len(salt)
       # assert isinstance(salt, str)

        if isinstance(password, unicode):
            password = password.encode('UTF-8')

        assert isinstance(password, str)
        result = HMAC(password, salt, sha256).hexdigest()
        return salt + result
    
    def checkPassword(self, username, passwd):
        db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME)
        cursor = db.cursor()
        cmd = 'SELECT password FROM user WHERE username="%s";' % cleanString(username)
        cursor.execute(cmd)
        rowUser = cursor.fetchone()
        if rowUser == None:
            return False
        crypted = rowUser[0]
        
        if crypted == self.encrypt_server_password(passwd, crypted[:salt_length]):
            return True
        else:
            return False
        db.close()

class ChangePasswd():
    def GET(self):
        if session.login != True:
            return render.message(site_prefix, "未登录", "您尚未登录", "", "_parent", "登录界面")
        return render.password(site_prefix, "修改密码")
    def POST(self):
        if session.login != True:
            return render.message(site_prefix, "未登录", "您尚未登录", "", "_parent", "登录界面")
        oldPasswd = web.input().oldpw
        newPasswd = web.input().newpw
        username = session.username
        if PasswordManager().checkPassword(username, oldPasswd):
            cryptedNew = PasswordManager().encrypt_server_password(newPasswd)
            self.updateNewPasswd(cryptedNew, username)
            session.login = False 
            session.kill()
            logger.info("IP: %s USER: %s Change passwd to %s successful." % (session.ip, username, newPasswd))
            return render.message(site_prefix, "密码修改成功", "密码修改成功，请重新登录", "", "_parent", "登录界面")
        else:
            return render.message(site_prefix, "密码修改失败", "原密码错误", "passwd", "main", "修改密码")

    def updateNewPasswd(self, newpasswd, username):
        db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME)
        cursor = db.cursor()
        cmd = 'UPDATE user SET password="%s"  WHERE username="%s";' % (cleanString(newpasswd), cleanString(username))
        cursor.execute(cmd)
        db.close()

if __name__ == "__main__":
    print PasswordManager().encrypt_server_password(18602800563)
