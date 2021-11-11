FROM alpine:3.10
#
RUN apk --no-cache add exim && \
    apk --no-cache add exim-dnsdb && \
    apk --no-cache add bind-tools && \
    #mkdir /var/log/exim /var/spool/exim /usr/lib/exim && \
	mkdir /var/spool/exim && \
    ln -sf /dev/stdout /var/log/exim/mainlog && \
    ln -sf /dev/stderr /var/log/exim/panic && \
    ln -sf /dev/stderr /var/log/exim/reject && \
    chown -R exim:exim /var/log/exim /var/spool/exim /usr/lib/exim && \
    chmod 0755 /usr/sbin/exim
#
COPY exim.conf /etc/exim/exim.conf
#
USER exim
EXPOSE 6025
#
ENV LOCAL_DOMAINS= \
    RELAY_FROM_HOSTS=10.0.0.0/8:172.16.0.0/12:192.168.0.0/16 \
    RELAY_TO_DOMAINS=* \
    RELAY_TO_USERS= \
	RELAY_SPF_REGEX_DOMAIN= \
	RELAY_MSGBODY_REGEX= \
	RELAY_MSGSUBJ_REGEX= \
    SMARTHOST= \
	SMARTHOSTPORT=25 \
	SENDER_MASK=* \
	RATE_INTERVAL= \
	RATE_VOLUME= \
	SIZE_LIMIT=1M \
    SMTP_PASSWORD= \
    SMTP_USERDOMAIN= \
    SMTP_USERNAME=
#
ENTRYPOINT ["exim", "-bdf", "-q15m"]
#ENTRYPOINT ["exim", "-bdf", "-q15m", "-d+all"]