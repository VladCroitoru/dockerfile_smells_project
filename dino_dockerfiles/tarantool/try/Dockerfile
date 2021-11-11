FROM tarantool/tarantool:1.8

RUN apk add --no-cache \
    ca-certificates \
    curl \
    openssl

ENV DOCKER_BUCKET get.docker.com
ENV DOCKER_VERSION 1.12.1
ENV DOCKER_SHA256 05ceec7fd937e1416e5dce12b0b6e1c655907d349d52574319a1e875077ccb79

RUN set -x \
    && curl -fSL "https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o docker.tgz\
    && echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \
    && tar -xzvf docker.tgz \
    && mv docker/* /usr/local/bin/ \
    && rmdir docker \
    && rm docker.tgz \
    && docker -v

RUN apk add --no-cache \
    btrfs-progs \
    e2fsprogs \
    e2fsprogs-extra \
    iptables \
    xfsprogs \
    xz \
    bash

# set up subuid/subgid so that "--userns-remap=default" works out-of-the-box
RUN set -x \
    && addgroup -S dockremap \
    && adduser -S -G dockremap dockremap \
    && echo 'dockremap:165536:65536' >> /etc/subuid \
    && echo 'dockremap:165536:65536' >> /etc/subgid

ENV DIND_COMMIT 3b5fac462d21ca164b3778647420016315289034

RUN wget "https://raw.githubusercontent.com/docker/docker/${DIND_COMMIT}/hack/dind" -O /usr/local/bin/dind \
    && chmod +x /usr/local/bin/dind

ENV DOCKER_HOST=tcp://127.0.0.1:12345

ADD https://github.com/jwilder/forego/releases/download/v0.16.1/forego /usr/local/bin/forego
RUN chmod u+x /usr/local/bin/forego
COPY Procfile /opt/tarantool

COPY start.lua /opt/tarantool/
COPY try/ /usr/local/share/tarantool/try/
COPY templates/ /usr/local/share/tarantool/try/templates/

COPY dockerd-entrypoint.sh /usr/local/bin/

VOLUME /var/lib/docker
EXPOSE 2375

ENTRYPOINT ["dockerd-entrypoint.sh"]
CMD ["forego", "start", "-r"]
