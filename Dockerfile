FROM python:alpine3.6

WORKDIR /app

ADD requirements.txt /app

RUN apk update && \
    apk add alpine-sdk

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn gevent

ADD src /app
ADD docker/run.sh /root

ENV ENVIRONMENT=prod

ENTRYPOINT ["/root/run.sh"]
