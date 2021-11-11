FROM alpine:latest
LABEL maintainer "marco@nelli.tech"

ADD https://pagekite.net/pk/pagekite.py /usr/local/bin
COPY docker-entrypoint.sh /usr/local/bin/
RUN set -ex; \
    apk --update --no-cache add python bash; \
    chmod +x /usr/local/bin/docker-entrypoint.sh; \
    chmod +x /usr/local/bin/pagekite.py;

VOLUME /root/
    
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 80

CMD ["pagekite.py", "--logfile=stdio"]
