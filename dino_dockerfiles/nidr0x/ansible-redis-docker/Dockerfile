FROM alpine:latest

MAINTAINER Carlos Rodríguez <nidr0x@gmail.com>

RUN apk add --update \
    ansible && \
    rm -rf /tmp/* && \
    rm -rf /var/cache/apk/*

COPY ansible/ /

RUN ansible-playbook -i "localhost," -c local /playbook.yml && \
    rm -rf /tmp/* && \
    rm -rf /var/cache/apk/*

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

VOLUME ["/data"]

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 6379