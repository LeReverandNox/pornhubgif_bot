#!/bin/sh

if [ $ENVIRONMENT == "prod" ]; then
    exec python /app/server.py
elif [ $ENVIRONMENT == "dev" ]; then
    exec python /app/server.py
fi
