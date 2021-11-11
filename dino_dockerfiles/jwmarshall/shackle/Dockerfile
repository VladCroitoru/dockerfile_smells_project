FROM alpine:latest
MAINTAINER Jonathon W. Marshall

RUN apk --update add bash bind bind-tools python py-jinja2 \
    && rm -rf /var/cache/apk/*

ADD generate_config.py /etc/bind/generate_config.py
ADD named.conf.jinja   /etc/bind/named.conf.jinja
ADD overrides          /var/bind/overrides
ADD run.sh             /run.sh

CMD ["/run.sh"]
