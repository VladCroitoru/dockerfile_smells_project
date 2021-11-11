FROM alpine:3.3

MAINTAINER Ryan C Koch "ryanckoch@gmail.com"

RUN apk add --update bash bind

ADD conf/named.conf /etc/bind/named.conf
ADD conf/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

CMD [ "/usr/sbin/named", "-c", "/etc/bind/named.conf", "-f" ]

ENTRYPOINT [ "/entrypoint.sh" ]
