FROM alpine

ENV RUN="busybox echo 'No command was defined. Extend this image or input command when creating image.'"

RUN apk --no-cache add socat  && \
    apk --no-cache --virtual .bootstrap add wget ca-certificates && \
    update-ca-certificates && \
    wget -O /tmp/docker.tgz https://get.docker.com/builds/Linux/x86_64/docker-17.05.0-ce.tgz && \
    tar -xzf /tmp/docker.tgz -C /tmp && \
    cp /tmp/docker/docker /bin/docker && \
    chmod +x /bin/docker && \
    apk del .bootstrap && \
    rm -rf /tmp/*

COPY start.sh /start.sh

ENTRYPOINT ["/start.sh"]