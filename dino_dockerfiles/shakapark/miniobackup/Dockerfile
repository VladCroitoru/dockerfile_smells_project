FROM alpine:3.7

RUN apk --no-cache add bash \
                       curl
RUN apk add --update --no-cache coreutils \
                                python \
                                python-dev \
                                py-pip \
    && pip install awscli

RUN curl  https://dl.minio.io/client/mc/release/linux-amd64/mc -o /usr/bin/mc && \
    chmod +x /usr/bin/mc

ADD entrypoint.sh /
RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
