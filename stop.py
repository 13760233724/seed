#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from config import *
PIDFILE = wwwpath + "seed.pid"
f = open(PIDFILE, "r")
pid = int(f.readline())
cmd = "kill -9 %d" % pid
os.system(cmd)