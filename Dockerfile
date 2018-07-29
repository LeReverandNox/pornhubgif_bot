FROM python:alpine3.6

WORKDIR /app


RUN apk update && \
    apk add alpine-sdk

RUN pip install pipenv
RUN pip install --no-cache-dir gunicorn gevent

ADD Pipfile /app
ADD Pipfile.lock /app
RUN pipenv install --system --deploy

ADD src /app
ADD docker/run.sh /root

ENV ENVIRONMENT=prod

ENTRYPOINT ["/root/run.sh"]
