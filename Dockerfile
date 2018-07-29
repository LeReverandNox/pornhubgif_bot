FROM python:alpine3.6

WORKDIR /app

ADD Pipfile /app

RUN apk update && \
    apk add alpine-sdk

RUN pip install pipenv
RUN pip install --no-cache-dir gunicorn gevent
RUN pipenv install --system --deploy

ADD src /app
ADD docker/run.sh /root

ENV ENVIRONMENT=prod

ENTRYPOINT ["/root/run.sh"]
