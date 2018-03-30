from bottle import request, response
from datetime import datetime
import sys

def logger_hook():
    log = '{} - [{}] "{} {} {}" {}'.format(
        request.environ.get('HTTP_X_FORWARDED_FOR') or request.remote_addr,
        datetime.now().strftime("%d/%b/%Y %H:%M:%S"),
        request.method,
        request.path,
        request.environ.get('SERVER_PROTOCOL'),
        response.status_code
    )
    sys.stdout.write('{} \n'.format(log))
