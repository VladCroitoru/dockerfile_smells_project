FROM alpine:3.2
MAINTAINER Calvin Leung Huang <https://github.com/cleung2010>

RUN apk --update add nodejs git openssh && \
    rm -rf /var/cache/apk/* && \
    npm install git2consul@0.12.10 --global && \
    mkdir -p /etc/git2consul.d

ADD config.json /etc/git2consul.d/config.json
ADD init.sh /init.sh
RUN chmod 700 /init.sh

ENTRYPOINT [ "/init.sh" ]
