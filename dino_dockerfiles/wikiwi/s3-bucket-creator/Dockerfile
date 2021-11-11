FROM alpine

LABEL org.label-schema.vcs-url="https://github.com/wikiwi/s3-bucket-creator" \
      org.label-schema.vendor=wikiwi.io \
      org.label-schema.name=s3-bucket-creator \
      io.wikiwi.license=MIT

RUN apk add --update \
    bash \
    ca-certificates \
    openssl \
    wget

RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.23-r3/glibc-2.23-r3.apk && \
    apk add glibc-2.23-r3.apk

RUN wget -O /usr/bin/mc https://dl.minio.io/client/mc/release/linux-amd64/mc && \
    chmod +x /usr/bin/mc

COPY run.sh /sbin/run.sh
RUN chmod 755 /sbin/run.sh

ENTRYPOINT ["/bin/bash"]
CMD ["/sbin/run.sh"]

