#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from hashlib import sha256
from hmac import HMAC 
import sys

#用于生成认证的密码
salt_length = 13
def encrypt_server_password(password, salt = None):
    if salt is None:
        matrix = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~!@#$%^&*"
        salt = ''.join(random.sample(matrix, salt_length))
    
    assert salt_length == len(salt)

    if isinstance(password, unicode):
        password = password.encode('UTF-8')

    result = HMAC(password, salt, sha256).hexdigest()
    return salt + result

if __name__ == "__main__":
    print encrypt_server_password(str(sys.argv[1]))