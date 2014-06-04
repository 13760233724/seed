#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
from config import *

app = web.application(urls, globals())
db = web.database(dbn = 'mysql', db = DB_NAME, user = DB_USER, pw = DB_PASSWORD)
store = web.session.DBStore(db, 'sessions')
session = web.session.Session(app, store, initializer = {'login': False, 'username' : 0})

def session_hook():
    web.ctx.session = session 

app.add_processor(web.loadhook(session_hook))

if __name__ == "__main__":
    app.run()