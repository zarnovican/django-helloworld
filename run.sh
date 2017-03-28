#!/bin/bash

if [ "$LOG_TARGET" == "syslog" -a ! -S /dev/log ]; then
    echo "Logging to syslog configured, but /dev/log not found!"
    exit -1
fi

/usr/local/bin/confd -backend env -onetime -confdir ./confd/ &&
exec uwsgi uwsgi.ini
