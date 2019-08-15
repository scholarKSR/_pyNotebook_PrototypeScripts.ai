#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 04:46:00 2019

@author: root
"""

"""
It's dangerous, so better sign this.

Various helpers to pass data to untrusted environments and to get it back safe 
and sound. Data is cryptographically signed to ensure that a token has not been
tampered with.

It's possible to customize how data is serialized. Data is compressed as needed. 
A timestamp can be added and verified automatically while loading a token.
"""

from itsdangerous import URLSafeSerializer

auth_s = URLSafeSerializer("secret key", "auth")
token = auth_s.dumps({"id": 5, "name": "itsdangerous"})

print(token)
# eyJpZCI6NSwibmFtZSI6Iml0c2Rhbmdlcm91cyJ9.6YP6T0BaO67XP--9UzTrmurXSmg

data = auth_s.loads(token)
print(data["name"])
# itsdangerous



# NoFirstUse
