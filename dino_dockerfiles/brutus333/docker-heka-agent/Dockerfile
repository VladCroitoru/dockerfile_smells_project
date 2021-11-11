FROM alpine:3.2

MAINTAINER Virgil Chereches <virgil.chereches@gmx.net>

ENV HEKA_TAG v0.10.0
ENV CONFD_VERSION=0.11.0


RUN apk -U add gcc musl-dev bzr mercurial git cmake go alpine-sdk bash perl && \
    git clone https://github.com/mozilla-services/heka.git && \
    cd /heka && \
    git checkout $HEKA_TAG && \
    bash -c "source ./build.sh && make package" && \
    tar xvzf /heka/build/heka-*.tar.gz -C /usr --strip-components=1 && \
    cd && rm -rf /heka && \
    git clone https://github.com/kelseyhightower/confd.git /src/confd && \
    cd /src/confd && \
    git checkout -q --detach "v$CONFD_VERSION" && \
    cd /src/confd/src/github.com/kelseyhightower/confd && \
    GOPATH=/src/confd/vendor:/src/confd go build -a -installsuffix cgo -ldflags '-extld ld -extldflags -static' -x . && \
    mv ./confd /bin/ && \
    chmod +x /bin/confd && \
    rm -rf /src && \
    apk del gcc musl-dev bzr mercurial git cmake go alpine-sdk bash perl && \
    rm -rf /var/cache/apk/*

COPY heka/*.toml /etc/heka/

COPY confd /etc/confd

COPY start.sh start.sh

VOLUME /var/run/docker.sock


ENTRYPOINT ["/start.sh"]
