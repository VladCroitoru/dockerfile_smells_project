FROM python:3.6-alpine

RUN apk add --no-cache git \
 && python3 -m pip install --upgrade radicale \
 && mkdir /data \
 \
 && adduser -S -D -h /data radicale radicale

COPY entrypoint.sh /usr/local/bin

EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
