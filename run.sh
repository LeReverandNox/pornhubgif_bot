#!/bin/sh

if [ $ENVIRONMENT == "prod" ]; then
    exec python /app/bot.py
elif [ $ENVIRONMENT == "dev" ]; then
    exec python /app/bot.py
fi
