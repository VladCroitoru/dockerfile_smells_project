FROM alpine:3.2
MAINTAINER ekozan

RUN echo "http://dl-1.alpinelinux.org/alpine/v3.2/main" >> /etc/apk/repositories && \
    echo "@testing http://dl-1.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    apk --update add docker-registry@testing && \
    rm -rf /var/cache/apk/*

VOLUME ["/var/lib/registry"]
EXPOSE 5000
ENTRYPOINT ["docker-registry"]
CMD ["/etc/docker-registry/config.yml"]
