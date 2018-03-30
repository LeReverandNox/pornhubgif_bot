#!/bin/sh

if [ $ENVIRONMENT == "prod" ]; then
    exec gunicorn -b 0.0.0.0:8080 -w 3 -k gevent --log-file - --log-level info --access-logfile - server:app
elif [ $ENVIRONMENT == "dev" ]; then
    exec gunicorn -b 0.0.0.0:8080 -w 3 -k gevent --log-file - --log-level debug --access-logfile - server:app
fi
