FROM respoke/asterisk:13.15

RUN rm /etc/asterisk/*
ADD etc/asterisk /etc/asterisk
ADD autoconfig-entrypoint.sh /

ENV BROKER_PORT=19000
ENV AMI_SECRET=verboice

CMD ["/usr/sbin/asterisk", "-f", "-n"]
ENTRYPOINT ["/autoconfig-entrypoint.sh"]
