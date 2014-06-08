#!/usr/bin/env python
# coding: utf-8
import web
from logger import *
from config import *
from functions import *
import time

session = web.ctx.session

class show:
    def GET(self):
        if session.login != True:
            return render.message(site_prefix, "未登录", "您尚未登录", "", "_parent", "登录界面")

        devices = getDevices();
        return render.manage(site_prefix, devices)


class add:
    def GET(self):
        if session.login != True:
            return render.message(site_prefix, "未登录", "您尚未登录", "", "_parent", "登录界面")
        types = getType()
        return render.add(site_prefix, types, "添加产品信息")

    def POST(self):
        if session.login != True:
            return render.message(site_prefix, "未登录", "您尚未登录", "", "_parent", "登录界面")
        productid = web.input().productid
        productname = web.input().productname
        brand = web.input().brand

        db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME)
        cursor = db.cursor()

        #cmd = "SELECT id FROM type WHERE name='%s';" % producttype
        #cursor.execute(cmd)
        #producttype = cursor.fetchone()[0]

        cmd = "SELECT * FROM devices WHERE id='%s' and brand='%s';" % (productid, brand)
        cursor.execute(cmd)
        rows = cursor.fetchall()

        if len(rows) != 0:
            db.close()
            return render.message(site_prefix, "添加失败", "该产品已经存在", "add", "main", "重新添加")

        else:
            now = time.strftime("%Y-%m-%d %H:%M:%S")
            cmd = "INSERT INTO devices (`seedid`, `name`, `brand`, `pos`, `lasttime`) VALUES ('%s', '%s', '%s', '%s', '%s');" % (cleanString(productid), cleanString(productname), cleanString(brand), '产品信息创建', now)
            cursor.execute(cmd)

            cmd = "INSERT INTO hispos (`seedid`, `pos`, `time`, `brand`) VALUES ('%s', '%s', '%s', '%s');" % (cleanString(productid), '产品信息创建', now, cleanString(brand))
            cursor.execute(cmd)
            db.close()
        
            return render.message(site_prefix, "添加成功", "新产品添加成功", "manage", "main", "产品管理")

class delete:
    def GET(self):
        if session.login != True:
            return render.message(site_prefix, "未登录", "您尚未登录", "", "_parent", "登录界面")
        id = web.input().id
        db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME)
        cursor = db.cursor()
        cmd = "DELETE FROM devices WHERE id='%s';" % id
        cursor.execute(cmd)

        cmd = "DELETE FROM hispos WHERE deviceid='%s';" % id
        cursor.execute(cmd)

        return render.message(site_prefix, "删除成功", "产品删除成功", "manage", "main", "产品管理")

class modify:
    def GET(self):
        if session.login != True:
            return render.message(site_prefix, "未登录", "您尚未登录", "", "_parent", "登录界面")
        id = web.input().id
        session.oldid = id
        devices = getDevices(id);
        types = getType()
        return render.modify(site_prefix, devices, types, "修改产品信息")

    def POST(self):
        if session.login != True:
            return render.message(site_prefix, "未登录", "您尚未登录", "", "_parent", "登录界面")
        seedid = web.input().productid
        productname = web.input().productname
        brand = web.input().brand   

        db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME)
        cursor = db.cursor()

        #cmd = "SELECT id FROM type WHERE name='%s';" % producttype
        #cursor.execute(cmd)
        #producttype = cursor.fetchone()[0]             

        #cmd = "SELECT * FROM devices WHERE id='%s' and brand='%s';" % (seedid, brand)
        #cursor.execute(cmd)
        #rows = cursor.fetchall()

        #if productid != session.oldid and len(rows) != 0:
        #    db.close()
        #    return render.message(site_prefix, "修改失败", "产品唯一标识重复", "modify?id=" + str(session.oldid), "main", "重新修改")

        #else:
        #now = time.strftime("%Y-%m-%d %H:%M:%S")
        cmd = "UPDATE devices SET seedid = '%s', name = '%s', brand = '%s' WHERE id = '%s'" % (seedid, productname, brand, session.oldid) 
        cursor.execute(cmd)
        db.close()
    

        return render.message(site_prefix, "修改成功", "产品信息修改成功", "manage", "main", "产品管理")   