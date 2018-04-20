#!/usr/bin/env python
#!coding=utf8
#Filename:backup_ver1.py


import os
import time

# 1. The files and directories to be backed up are specified in a list
source = ['/var/log/mesh/pytest/a', '/var/log/mesh/pytest/b']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that

# 2. The backup must be stored in a main backup directory
target_dir = '/var/log/mesh/pytest/bak/'

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the sub directory in the main directory
today = target_dir + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')
# Create the sub directory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successful created directory', today

# The name of the zip file
target = today + os.sep + now + '.zip'

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr '%s'%s" % (target, ''.join(source))
tar = 'tar -zvcf %s%s -X /var/log/mesh/pytest/a/hcp.xls' % (target, ''.join(source))

# Run the backup
if os.system(tar) == 0:
    print 'Successful backup to', target
else:
    print 'Backup failure'
