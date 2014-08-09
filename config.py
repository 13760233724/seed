#!/usr/bin/env python
# coding: utf-8
import web
import logging

site_prefix = "/seed"
wwwpath = "/home/www/seed/"
site_title = "中国电信种联网溯源套件综合业务平台"
DB_HOST =       "localhost"
DB_NAME =       "product"
DB_USER =       "product"
DB_PASSWORD =   "product"

AVATAR_MAXUPLOAD = 1 # 头像文件大小上限,单位MB
WORKFILE_MAXUPLOAD = 30 # 头像文件大小上限,单位MB

render = web.template.render('template/', cache = False)
web.config.debug = False
web.config.session_parameters['timeout'] = 1800  #session过期时间30分钟
#web.config.session_parameters['ignore_expiry'] = False

urls = (
    site_prefix,                      'login.login',
    site_prefix + '/',                'login.login',
    site_prefix + '/login',           'login.login',
    site_prefix + '/logout',          'logout.logout',
    site_prefix + '/mktop',           'main.MakeTop',
    site_prefix + '/mkmenu',          'main.MakeMenu',
    site_prefix + '/passwd',          'password.ChangePasswd',
    site_prefix + '/changepasswd',    'password.ChangePasswd',
    site_prefix + '/register',        'register.Register',
    site_prefix + '/welcome',         'main.welcome',
    site_prefix + '/view',            'view.view',
    site_prefix + '/viewhispos',      'view.viewhispos',
    site_prefix + '/manage',          'manage.show',
    site_prefix + '/add',             'manage.add',
    site_prefix + '/delete',          'manage.delete',
    site_prefix + '/modify',          'manage.modify',
    site_prefix + '/api',             'api.index',
    site_prefix + '/zlwview',         'view.directview',
    site_prefix + '/zlw',             'login.noverify',
)

logfile = "logs/portable.log"
LOG_LEVEL = logging.DEBUG
