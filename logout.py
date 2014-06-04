#!/usr/bin/env python
# coding: utf-8
import web
from logger import *
from config import *

session = web.ctx.session

class logout:
    def GET(self):
        if session.login != True:
            raise web.seeother(site_prefix + "/")
        try:
            session.login = False
            session.kill()
        except AttributeError:
            pass 
        logger.info("IP: %s USERNAME: %s Logout." % (session.ip, session.username))
        raise web.seeother(site_prefix + "/")
