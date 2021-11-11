FROM gliderlabs/alpine:3.4

MAINTAINER Hang Yan <hangyan@hotmail.com>

RUN apk update && apk add htop nano bash curl busybox && rm -rf /var/cache/apk/*

COPY run.sh /

RUN chmod a+x /run.sh && \
    mkdir /web && echo "I'm ok" >> /web/index.html && \
    echo "alias ll='ls -l'" >> ~/.bashrc

EXPOSE 9527

CMD ["/run.sh"]
