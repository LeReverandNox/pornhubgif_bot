FROM python:alpine3.6

WORKDIR /app

ADD requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

ADD src /app
ADD docker/run.sh /root

ENV ENVIRONMENT=prod

ENTRYPOINT ["/root/run.sh"]
