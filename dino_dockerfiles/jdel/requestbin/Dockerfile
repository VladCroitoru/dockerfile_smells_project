FROM python:2.7-alpine

COPY requirements.txt /opt/requestbin/
COPY requestbin /opt/requestbin/requestbin/
WORKDIR /opt/requestbin

RUN apk add --update python gcc python-dev py-pip \
    # greenlet
    musl-dev \
    # sys/queue.h
    bsd-compat-headers \
    # event.h
    libevent-dev \
 && apk upgrade \
 && pip install -r /opt/requestbin/requirements.txt \
 && rm -rf ~/.pip/cache \
 && rm -rf /var/cache/apk/*

EXPOSE 8000

CMD gunicorn -b 0.0.0.0:8000 --worker-class gevent --workers 1 --max-requests 1000 requestbin:app
