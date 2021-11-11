FROM alpine:edge
MAINTAINER Tobias Haber <kontakt@t-haber.de>


RUN apk add --update \
    samba-common-tools \
    samba-client \
    samba-server \
    bash \
    samba \
    && rm -rf /var/cache/apk/*

RUN rm -f /etc/samba/smb.conf

ADD smb.conf /smb.conf.full
RUN echo "* soft nofile 16384" >> /etc/security/limits.conf
RUN echo "* hard nofile 16384" >> /etc/security/limits.conf

RUN testparm -s /smb.conf.full > /etc/samba/smb.conf

EXPOSE 445/tcp
EXPOSE 139/tcp
EXPOSE 138/udp
EXPOSE 137/udp
ADD start.sh /bin/start.sh
RUN chmod a+x /bin/start.sh
CMD ["./bin/start.sh"]
