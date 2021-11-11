FROM alpine:3.3
MAINTAINER Luis Alonzo <wichon@gmail.com>
LABEL Description="Easy to use SSH Tunnel based in the Alpine Linux docker image"

RUN apk --update add openssh-client \
    && rm -f /var/cache/apk/*

# Security fix for CVE-2016-0777 and CVE-2016-0778
RUN echo -e 'Host *\nUseRoaming no' >> /etc/ssh/ssh_config \
    && mkdir ~/.ssh

ADD start.sh app/

RUN chmod +x /app/start.sh

ENTRYPOINT ["/app/start.sh"]
