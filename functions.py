#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
from config import *
from logger import *

def getTruename(username):
    db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME, charset='utf8')
    cursor = db.cursor()
    cmd = 'SELECT name FROM user WHERE username="%s";' % username
    cursor.execute(cmd)
    rowUser = cursor.fetchone()
    if rowUser == None:
        return ""
    db.close()
    return rowUser[0]

def cleanString(data):
    data = data.encode('utf-8')
    return MySQLdb.escape_string(data)

def getRealId(seedid, brand):
    db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME, charset='utf8')
    cursor = db.cursor()
    cmd = "SELECT * FROM devices WHERE seedid = %s and brand = '%s'" % (seedid, brand)
    cursor.execute(cmd)
    result = cursor.fetchone()
    try:
        if len(result) != 0:
            return result[0]
        else:
            return -1
    except:
        return -1

def getHisPos(deviceid):
    db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME, charset='utf8')
    cursor = db.cursor()
    cmd = 'SELECT * FROM hispos WHERE deviceid = %s ORDER BY time DESC' % deviceid
    cursor.execute(cmd)
    result = cursor.fetchall()
    hispos = [] 
    for row in result:
        id = row[1]
        pos = row[2]
        postime = row[3]
        hispos.append([id, postime, pos])

    return hispos

def getDevices(deviceid = -1):
    db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME, charset='utf8')
    cursor = db.cursor()
    if deviceid == -1:
        cmd = 'SELECT * FROM devices;'
    else:
        cmd = 'SELECT * FROM devices WHERE id = %s' % deviceid
    cursor.execute(cmd)
    result = cursor.fetchall()
    devices = {}
    for row in result:
        id = row[0]
        devicename = row[1]

        brand = row[2]

        userid = row[3]
        userid = userid.split('|')
        users = []
        for each in userid:
            if each == "":
                continue
            cmd = 'SELECT name FROM deviceuser WHERE id = %s;' % each
            cursor.execute(cmd)
            users.append(cursor.fetchone()[0])

        binduserid = row[4]
        binduserid = binduserid.split('|')
        bindusers = []
        for each in binduserid:
            if each == "":
                continue
            cmd = 'SELECT name FROM deviceuser WHERE id = %s;' % each
            cursor.execute(cmd)
            bindusers.append(cursor.fetchone()[0])

        groupid = row[5]
        groupid = groupid.split('|')
        groups = []
        for each in groupid:
            if each == "":
                continue
            cmd = 'SELECT name FROM groups WHERE id = %s;' % each
            cursor.execute(cmd)
            groups.append(cursor.fetchone()[0])

        statusid = row[8]
        cmd = 'SELECT statusname FROM status WHERE id = %s;' % statusid
        cursor.execute(cmd)
        status = cursor.fetchone()[0]

        lasttime = row[9]

        data = row[6]
        pos = row[7]

        seedid = row[10]
        

        onedevice = [id, devicename, brand, users, bindusers, groups, status, lasttime, data, pos, seedid]
        devices[id] = onedevice
    
    db.close()
    return devices


def getType(typeid = -1):
    db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME, charset='utf8')
    cursor = db.cursor()
    if typeid == -1:
        cmd = 'SELECT * FROM type;'
    else:
        cmd = 'SELECT * FROM type WHERE id = %s' % typeid
    cursor.execute(cmd)
    result = cursor.fetchall()
    types = {}
    for row in result:
        id = row[0]
        typename = row[1]

        onetype = [id, typename]
        types[id] = onetype
    
    db.close()
    return types

def getproductstatus(statusid = -1):
    db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME, charset='utf8')
    cursor = db.cursor()
    if statusid == -1:
        cmd = 'SELECT * FROM status;'
    else:
        cmd = 'SELECT * FROM status WHERE id = %s' % statusid
    cursor.execute(cmd)
    rows = cursor.fetchall()
    status = {}
    for everyone in rows:
        status[everyone[0]] = everyone[1]
    return status
