FROM telegraf:1.6-alpine
RUN apk add -U curl
COPY entrypoint.sh /entrypoint.sh
COPY telegraf.conf /etc/telegraf/
