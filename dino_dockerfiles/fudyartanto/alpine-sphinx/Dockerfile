FROM alpine:3.6

RUN apk add --no-cache \
  sphinx \
  php7 \
  supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir -p /var/log/supervisor
RUN mkdir -p /var/run/supervisor

COPY config/sphinx/sphinx.conf /etc/sphinx/sphinx.conf 

RUN mkdir /src
WORKDIR /src

EXPOSE 9306

ENTRYPOINT ["/usr/bin/supervisord", "--nodaemon", "--configuration", "/etc/supervisor/conf.d/supervisord.conf","--logfile", "/var/log/supervisor/supervisord.log","--pidfile", "/var/run/supervisor/supervisord.pid"]
