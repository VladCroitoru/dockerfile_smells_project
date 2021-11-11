FROM alpine:3.6

RUN apk --no-cache add exim mailx bash && \
    mkdir /var/log/exim /var/spool/exim /usr/lib/exim && \
    chown -R exim:exim /var/log/exim /var/spool/exim /usr/lib/exim && \
    chmod 0755 /usr/sbin/exim

COPY exim.conf /etc/exim/exim.conf

ENV LOCAL_DOMAINS=@ \
    RELAY_FROM_HOSTS=10.0.0.0/8:172.16.0.0/12:192.168.0.0/16 \
    RELAY_TO_DOMAINS=* \
    RELAY_TO_USERS= \
    SMARTHOST= \
    SMTP_PASSWORD= \
    SMTP_USERDOMAIN= \
    SMTP_USERNAME=

ENTRYPOINT exim -bdf -q15m 
