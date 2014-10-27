#!/usr/bin/python
### Check if the backup wal-e postgres is executed in the last day

import subprocess
import sys
from datetime import datetime, timedelta
import time

command = "/usr/bin/envdir /etc/wal-e.d/env /usr/local/bin/wal-e backup-list | tail -1"

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
last =  output

last_string = last.split()[1][:-5]
last_datetime = datetime.strptime(last_string, "%Y-%m-%dT%H:%M:%S")
#print last_datetime

last_expected = datetime.now() - timedelta(hours=28)
#print last_expected

if last_datetime < last_expected:
    print "CRITICAL: Ultimo backup en  wal-e es de mas de un dia, el ultimo es de: %s !" % last_datetime
else:
    print "OK. Backup correcto. Ultimo backup es de: %s" % last_datetime
 

