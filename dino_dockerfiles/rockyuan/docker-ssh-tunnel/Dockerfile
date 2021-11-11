FROM alpine:latest

MAINTAINER "RockYuan" <RockYuan@gmail.com>

LABEL Description="在Docker的alpine镜像中建立SSH隧道"

RUN apk --update add openssh-client \
    && rm -f /var/cache/apk/*

# Security fix for CVE-2016-0777 and CVE-2016-0778
RUN echo -e 'Host *\nUseRoaming no\nServerAliveInterval 30\nServerAliveCountMax 20\nTCPKeepAlive no' >> /etc/ssh/ssh_config \
    && mkdir ~/.ssh

ADD start.sh app/

RUN chmod +x /app/start.sh

ENTRYPOINT ["/app/start.sh"]
