#!/usr/bin/env python
#!coding=utf8
#Filename:backup_ver1.py


import os
import time

# 1. The files and directories to be backed up are specified in a list
source = ['/var/log/mesh/pytest/a','/var/log/mesh/pytest/b']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that

# 2. The backup must be stored in a main backup directory
target_dir = '/var/log/mesh/pytest/bak'

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the




