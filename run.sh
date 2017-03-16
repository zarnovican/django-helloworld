#!/bin/bash

# if /dev/log is not mapped to container, override LOG_TARGET
[ ! -S /dev/log ] && export LOG_TARGET=console

/usr/local/bin/confd -backend env -onetime -confdir ./confd/ &&
exec uwsgi uwsgi.ini
