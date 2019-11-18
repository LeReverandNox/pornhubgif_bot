#!python3

import requests as r
import os, sys, argparse
from dotenv import load_dotenv, find_dotenv; load_dotenv(find_dotenv())

parser = argparse.ArgumentParser(description='Set the webhook URL of your bot.')
parser.add_argument('webhook_url', help='The url of your webhook endpoint')
parser.add_argument('--api-token', help='Your bot Telegram API token.', default=os.getenv('TELEGRAM_API_TOKEN'))
args = parser.parse_args()

if not args.api_token:
    exit('[ERROR] Please set your TELEGRAM_API_TOKEN in the .env file or use --api-token.')

TELEGRAM_API_URL = 'https://api.telegram.org/bot' + args.api_token

payload = {
    'url': args.webhook_url
}
res = r.post(TELEGRAM_API_URL + '/setWebhook', json=payload)
sys.stdout.write('[{}] {}\n'.format(res.status_code, res.json()['description']))
