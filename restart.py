#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from config import *
cmd = "python " + wwwpath + "stop.py"
os.system(cmd)
cmd = "python " + wwwpath + "start.py"
os.system(cmd)