#!/bin/bash

if [ "$LOG_TARGET" == "syslog" -a ! -S /dev/log ]; then
    echo "Logging to syslog configured, but /dev/log not found! Falling back to console."
    export LOG_TARGET=console
fi

/usr/local/bin/confd -backend env -onetime -confdir ./confd/ &&
exec uwsgi uwsgi.ini
