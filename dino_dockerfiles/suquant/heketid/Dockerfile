FROM alpine:3.7
MAINTAINER George Kutsurua <g.kutsurua@gmail.com>

ENV VERSION="6.0.0"

RUN wget https://github.com/heketi/heketi/releases/download/v${VERSION}/heketi-v${VERSION}.linux.amd64.tar.gz && \
    tar -xzvf heketi-v${VERSION}.linux.amd64.tar.gz && \
    mv /heketi/heketi /usr/bin/ && \
    mv /heketi/heketi-cli /usr/bin/ && \
    rm -rf /heketi heketi-v${VERSION}.linux.amd64.tar.gz && \
    mkdir /lib64 && ln -s /lib/ld-musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2

COPY ["entrypoint.sh", "/"]

VOLUME ["/var/lib/heketi"]

ENTRYPOINT ["/entrypoint.sh"]
CMD ["--config=/etc/heketi/heketi.json"]

EXPOSE 8080