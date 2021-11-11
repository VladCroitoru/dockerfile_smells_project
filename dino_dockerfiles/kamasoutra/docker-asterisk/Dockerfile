FROM alpine:latest

LABEL maintainer="Jean-Pierre Palik - kama@palik.fr" \
      description="Simple preconfigured Asterisk container for tests" \
      version="1.2"

RUN apk add --update asterisk asterisk-speex asterisk-sample-config asterisk-curl asterisk-srtp asterisk-sounds-en asterisk-sounds-moh

COPY *.conf /tmp/

RUN cat /tmp/users.conf >> /etc/asterisk/users.conf && \
    cat /tmp/extensions.conf >> /etc/asterisk/extensions.conf && \
    rm /tmp/*.conf

EXPOSE 5060 10000-20000

CMD ["/usr/sbin/asterisk", "-vvvdddf", "-T", "-W", "-U", "root", "-p"]
