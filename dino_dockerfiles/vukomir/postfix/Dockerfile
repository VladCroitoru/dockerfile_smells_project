FROM alpine:latest

MAINTAINER Vucomir Ianculov <vukomir@ianculov.ro>

# Install Packages
RUN true && apk add --no-cache --update ca-certificates postfix supervisor rsyslog mailx bash

# Clean up to save space
RUN rm "/tmp/"* 2>/dev/null || true && rm -rf /var/cache/apk/* 2>/dev/null || true

#configure postfix
ADD docker/postfix/config/main.cnf /etc/postfix/main.cf

#Configure supervisor
ADD docker/postfix/config/supervisord.conf /etc/supervisord.conf
ADD docker/postfix/config/supervisord /etc/supervisor/conf.d

#Setup docker
ADD docker/postfix/init /init
ADD docker/docker-entrypoint.sh /docker-entrypoint.sh

WORKDIR	/

EXPOSE 25

ENTRYPOINT ["/docker-entrypoint.sh"]
