#!/usr/bin/env python
# -*- coding: utf-8 -*_
import os
from config import *
cmd = "nohup python " + wwwpath + "index.py 8088 &"
os.system(cmd)
