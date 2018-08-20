#!/bin/sh

## add default crontab
## shutdown 

USER ='root'

echo "15 06  * * 1 /bin/sync;/bin/sync;/sbin/poweroff" >> "/var/spool/cron/$USER"
## enable random_range.sh
echo "05 00  * * * /bin/sh /root/python_conf/random_range.sh > /dev/null 2>&1" >> "/var/spool/cron/$USER"

## crontab apply
/usr/bin/crontab /var/spool/cron/$USER

