FROM frolvlad/alpine-glibc:3.2

ENV NOMAD_VERSION=0.2.3 \
    NOMAD_SHA256=2de82ab923e93a91ce772caab6a4b96964269891fc413b380e270cfcee540586
RUN apk add --update ca-certificates wget curl && \
    wget -O /nomad_${NOMAD_VERSION}_linux_amd64.zip https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_linux_amd64.zip && \
    echo "${NOMAD_SHA256}  nomad_${NOMAD_VERSION}_linux_amd64.zip" > /nomad.sha256 && \
    cd /usr/local/bin && \
    unzip /nomad_${NOMAD_VERSION}_linux_amd64.zip && \
    curl -o /usr/local/bin/docker https://get.docker.com/builds/Linux/x86_64/docker-1.9.1 && \
    chmod +x /usr/local/bin/docker && \
    wget -O /usr/local/bin/docker-compose https://github.com/docker/compose/releases/download/1.6.0/docker-compose-Linux-x86_64 && \
    chmod +x /usr/local/bin/docker-compose && \
    apk add git && \
    apk del ca-certificates wget && \
    rm -rfv /nomad* /var/cache/apk/*

ADD nomad.config /etc/nomad.config
ADD server.config /etc/server.config
ENTRYPOINT ["/usr/local/bin/nomad"]
VOLUME [ "/data" ]

# sha256sum -c /nomad.sha256 && \
