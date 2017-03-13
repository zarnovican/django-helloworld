#!/bin/bash

# if /dev/log is not mapped to container, override LOG_TARGET
[ ! -S /dev/log ] && export LOG_TARGET=console

exec uwsgi uwsgi.ini
