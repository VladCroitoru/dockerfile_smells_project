FROM alpine:3.5

ARG BATS_VERSION=0.4.0
ARG DOCKER_BUCKET=get.docker.com
ARG DOCKER_VERSION=1.13.1

RUN apk add --no-cache bash curl \
 && curl -o "/tmp/v${BATS_VERSION}.tar.gz" -L "https://github.com/sstephenson/bats/archive/v${BATS_VERSION}.tar.gz" \
 && tar -xzvf "/tmp/v${BATS_VERSION}.tar.gz" -C /tmp/ \
 && bash "/tmp/bats-${BATS_VERSION}/install.sh" /usr/local \
 && curl -fSL "https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o /tmp/docker.tgz \
 && tar -xzvf /tmp/docker.tgz -C /tmp/ \
 && mv /tmp/docker/docker /usr/local/bin/ \
 && rm -rf /tmp/*

VOLUME /work

WORKDIR /work

ENTRYPOINT ["/usr/local/bin/bats"]

CMD ["-v"]
