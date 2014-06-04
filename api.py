#!/usr/bin/env python
# coding: utf-8
import web
import MySQLdb
from logger import *
from config import *
from functions import *
from password import *
import time
import json

class index:
    def GET(self):
        try:
            method = web.input().method
            if method == "getstatus":
                return self.getstatus()
            if method == "getproductinfo":
                logger.info(str(web.input()))
                productid = web.input().id
                return self.getproductinfo(productid)
            else:
                return "未提供的方法"
        except Exception, e:
            logger.info(e)
            return "接口格式不正确"

    def POST(self):
        try:
            method = web.input().method
            if method == "login":
                username = web.input().username
                password = web.input().password
                return self.logincheck(username, password)
            if method == "uploadinfo":
                productid = int(web.input().id)
                statusid = int(web.input().statusid)
                return self.uploadinfo(productid, statusid)
            else:
                return "未提供的方法"
        except Exception, e:
            logger.info(e)
            return "接口格式不正确"

    def getstatus(self):
        return json.dumps(getproductstatus())

    def getproductinfo(self, productid):
        result = {}
        product = getDevices(productid)
        if len(product) == 0:
            result["code"] = 0
            result["content"] = "未检索该产品的相关信息"
            return json.dumps(result)

        result["code"] = 1
        result["content"] = {}

        product = product[int(productid)]
        name = product[1]
        type = product[2]
        result["content"]["name"] = name
        result["content"]["type"] = type

        db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME)
        cursor = db.cursor()
        cmd = 'SELECT * FROM hispos WHERE deviceid = %s ORDER BY time DESC' % productid
        cursor.execute(cmd)
        rows = cursor.fetchall()
        resultstr = ""
        for row in rows:
            pos = row[2]
            postime = row[3]
            resultstr += str(postime)
            resultstr += "\n"
            resultstr += str(pos)
            resultstr += "\n"

        result["content"]["info"] = resultstr
        db.close()
        return json.dumps(result)

    def uploadinfo(self, productid, statusid):
        result = {}
        product = getDevices(productid)
        if len(product) == 0:
            result["code"] = 0
            result["content"] = "该产品不存在"
            return json.dumps(result)
        status = getproductstatus(statusid)
        status = str(status[statusid])
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME)
        cursor = db.cursor()
        try:
            cmd = "UPDATE devices SET pos='%s',lasttime ='%s' WHERE id='%s';" % (status, now, productid)
            cursor.execute(cmd)
            cmd = "INSERT INTO hispos (`deviceid`, `pos`, `time`) VALUES ('%s', '%s', '%s');" % (productid, status, now)
            cursor.execute(cmd)
        except:
            pass
        db.close()
        result["code"] = 1
        result["content"] = "流转信息上传成功"
        return json.dumps(result)

    def logincheck(self, username, password):
        result = {}
        if username != None and password != None:
            if PasswordManager().checkPassword(username, password):
                logger.info("IP: %s USER: %s Login Successful." % (session.ip, username))
                now = time.strftime("%Y-%m-%d %H:%M:%S")
                db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME)
                cursor = db.cursor()
                cmd = "UPDATE user SET lasttime ='%s' WHERE username='%s';" % (now, username)
                cursor.execute(cmd)
                db.close()
                result["result"] = 1
                result["description"] = "登录成功"
                return json.dumps(result)
            else:
                result["result"] = 0
                result["description"] = "登录失败，用户名或密码错误"
                return json.dumps(result)  